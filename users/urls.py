from django.contrib import admin
from django.urls import path
from survey.views import questionnaire, landingpage, dashboard
from .views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('questionnaire', questionnaire, name='questionnaire'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', landingpage, name='landingpage'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]