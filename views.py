from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
import json
from django.urls import reverse
from .models import PainRecord
from django.contrib import messages

# Signup View & Login View & Forgotten Password
#Signing up to the pain tracking web application
def signup_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username has already been taken"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return JsonResponse({"message": "Signup is successful"}, status=201)

    return render(request, "signup.html")

#Logging into the pain tracking web application
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful", "redirect": "/"}, status=200)
        else:
            return JsonResponse({"message": "Invalid Username or Password"}, status=401)

    return render(request, "login.html")

#If forgotten the user can type in the email
def forgot_password(request):
    return render(request, 'forgot_password.html')

#Recieves the email
def reset_password_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "Reset email sent"}, status=200)
        else:
            return JsonResponse({"message": "Email not found"}, status=404)

    return JsonResponse({"message": "Invalid request"}, status=400)

    
#Navigation for Home, Contact, Setting, and Logout
#HomePage
@login_required
def HomePage(request):
    show_gdpr = not request.session.get('gdpr_accepted', False)
    return render(request, 'HomePage.html', {'show_gdpr': show_gdpr}) 

#Privacy policy expanded from GDPR
def privacy_policy(request):
    return render(request, 'privacy_policy.html')

#Accepting the GDPR
@csrf_exempt
def accept_gdpr(request):
    if request.method == "POST":
        request.session['gdpr_accepted'] = True
        return JsonResponse({"message": "GDPR accepted"})
#settings
@login_required
def settings(request):
    if request.method == "POST":
        if 'new_password' in request.POST:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user) 
    return render(request, "settings.html")

#Deleting the account
@login_required
def deactivate_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        
        if user:
            request.user.delete()
            logout(request)
            messages.success(request, "Your account has been deactivated.")
            return redirect('signup')
        else:
            messages.error(request, "Password is incorrect. Please try again.")
            return redirect('settings')

#contacts
def contact(request):
    if request.method == "POST":
        name = request.POST.get("support_name")
        email = request.POST.get("support_email")
        message = request.POST.get("support_message")
        return render(request, "contact.html", {'success': True})
    return render(request, "contact.html")

# Logout  and to choose to either log out or stay logged in
def logout_depths(request):
    return render(request, 'logout.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('HomePage')

#Sidebar for HomePage includes About-us, Guidance, History, and Dashboard
#About-Us
def About_Us(request):
    return render(request, 'About-Us.html') 

#Guidance for aiding users with each pain symptoms
def Guidance_view(request):
    return render(request, 'Guidance-page.html')

#searching for results
def search_results(request):
    query = request.GET.get('query', '').lower()  

    if query == 'settings':
        return redirect(reverse('settings'))  
    elif query == 'dashboard':
        return redirect(reverse('dashboard'))  

    return render(request, 'search_results.html', {'query': query, 'message': 'No matching pages found.'})

#Pain History to see examples of other pain symptoms to an idea
def History(request):
    return render(request, 'History.html')

#dashboard
def dashboard(request):
    if request.method == 'POST':
        pain_type = request.POST.get('pain_type')
        severity = request.POST.get('severity')
        duration = request.POST.get('duration')
        location = request.POST.get('location')
        trigger = request.POST.get('trigger')
        
        # PainRecord - in order to create and make new records
        PainRecord.objects.create(
            pain_type=pain_type,
            severity=severity,
            duration=duration,
            location=location,
            trigger=trigger,
        )
        return redirect('dashboard')  # Returns to the dashboard after tracking
    
    # Able to records all the pain types
    records = PainRecord.objects.all()
    return render(request, 'dashboard.html', {'records': records})

# For deleting a record
def delete_pain(request, id):
    record = PainRecord.objects.get(id=id)
    record.delete()
    return redirect('dashboard')

#All of the pain symptoms mentioned in the HomePage
#chest pain
def Chest_Pain(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'ChestPain.html') 

#back pain
def Back_Pain(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'BackPain.html') 

#Headache pain
def Headache_Pain(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'Headache.html') 

#Joint pain
def Joint_Pain(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'Joint.html') 

#Abdominal pain
def Abdominal_Pain(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'Abdominal_Pain.html') 


