"""ninjas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from equipos import views
from django.contrib.auth import views as auth_views

# Importar las vistas genericas ofrecidas por django para resetear contraseña
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
    ) # En confirm debe ir un token buscar como hacerlo en 2.0}
    # NOTA: No tengo ni idea, usar url de 1.11
    # NOTA2: Usar re_path
    # Token: (?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipo_edit/', views.equipo_view, name = 'equipo_edit'),
    path('signup/', views.signup_view, name = 'singup_view'),
    path('register/', views.signup_user_view, name = 'register_view'),
    path('login/', auth_views.login, {'template_name': 'equipos/login.html'}, name = 'login'),
    # path('perfil/', views.profile, name = "profile_view"),
    path('index/', views.index, name = "index_view"),
    path('profile/', views.view_profile, name = "profile_view"),
    path('logout/', auth_views.logout, {'template_name':'equipos/logout.html'}, name='logout'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile_view'),
    path('change_password/', views.change_password, name = 'change_password_view'),
    re_path(r'^password_reset/$', password_reset, {'template_name':'reset/password_reset_form.html',
    'email_template':'reset/password_reset_email.html'}, name = 'password_reset'),
    re_path(r'^password_reset_done/$', password_reset_done, {'template_name':'reset/password_reset_done.html',},
    name = 'password_reset_done'),
    re_path(r'^password_reset_confirm/$', password_reset_confirm, {'template_name':'reset/password_reset_confirm.html',},
    name = 'password_reset_confirm'),
    re_path(r'^password_reset_complete/$', password_reset_complete, {'template_name':'reset/password_reset_complete.html',},
    name = 'password_reset_complete'),
]
