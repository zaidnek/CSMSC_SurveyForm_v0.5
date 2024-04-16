from django.contrib import admin
from django.urls import path, include
from survey.views import questionnaire, confirmation, landing_page, dashboard, qrcode, qr, UserResponseListView
from users.views import RegisterView
from django.contrib.auth import views as auth_views
from survey.admin import custom_admin_site

urlpatterns = [
    path('questionnaire', questionnaire, name='questionnaire'),
    path('confirmation/', confirmation, name='confirmation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('listview/', UserResponseListView.as_view(), name='listview'),
    path('', qrcode, name='qrcode'), 
    path('qr', qr, name='qr'),    
    path('admin/', custom_admin_site.urls),
    path('accounts/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('landingpage/', landing_page, name='landingpage'),
]