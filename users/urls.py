from django.contrib import admin
from django.urls import path
from survey.views import questionnaire, landing_page, dashboard, qrcode, qr, UserResponseListView
from .views import RegisterView
from django.contrib.auth import views as auth_views
from survey.admin import custom_admin_site

urlpatterns = [
    path('questionnaire', questionnaire, name='questionnaire'),
    path('', qrcode, name='qrcode'),
    path('qr', qr, name='qr'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', custom_admin_site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('listview/', UserResponseListView.as_view(), name='listview'),
    path('landingpage/', landing_page, name='landingpage'),
]