from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('', views.login, name='login'),
    path('', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.signup, name='signup'),
    path('', views.dashboard, name='dashboard'),
]
