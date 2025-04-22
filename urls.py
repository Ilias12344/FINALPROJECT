from django.urls import path 
from . import views

urlpatterns = [ 
    path('HomePage/', views.HomePage, name='HomePage'), #HomePage where all possible information is found
    path('HomePage/dashboard/', views.dashboard, name='dashboard'), #Dashboard looks at the stats of pain tracking
    path('HomePage/settings/', views.settings, name='settings'), #Settings to help change user information
    path('HomePage/contact/', views.contact, name='contact'), #Contact for support those who need assisstance
    path('HomePage/About-Us/', views.About_Us, name='About-Us'),  #Information regarding us
    path('login/', views.login_view, name='login'), #Login with username and password
    path('signup/', views.signup_view, name='signup'), #Signup if you don't have an account
    path('forgot-password/', views.forgot_password, name='forgot_password'), #Forotten Password if you don't remember password
    path("reset-password/", views.reset_password_view, name="reset_password"), #The reset link sent to the user
    path('logout/', views.logout_depths, name='logout_depths'), #Logout if you wish so after logging in
    path('logout-yes,Logout-or-Cancel/', views.logout_view, name='logout'), #options before logging out
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'), #Part of GDPR
    path('accept_gdpr/', views.accept_gdpr, name='accept_gdpr'), #Important for the users to accept
    path('History/', views.History, name='History'), #represents fictious data for users to understand how to track
    path('chest/', views.Chest_Pain, name='Chest_Pain'), #type of pain symptom part of the web application
    path('BackPain/', views.Back_Pain, name='Back_Pain'), #type of pain symptom part of the web application
    path('Headache/', views.Headache_Pain, name='Headache_Pain'), #type of pain symptom part of the web application
    path('Joint/', views.Joint_Pain, name='Joint_Pain'), #type of pain symptom part of the web application
    path('Abdominal_Pain/', views.Abdominal_Pain, name='Abdominal_Pain'), #type of pain symptom part of the web application
    path('Guidance/', views.Guidance_view, name='Guidance'), # Guides the individual in tracking or to delete from the records.
    path('search/', views.search_results, name='search_results'), #Search bar part of the Guidance page.
    path('delete_pain/<int:id>/', views.delete_pain, name='delete_pain'), #To delete the pain symptoms.
    path('deactivate/', views.deactivate_account, name='deactivate_account'), #To delete the user's account
]