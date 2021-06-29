"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'MyBlog ADMIN'
admin.site.site_title = 'MyBlog ADMIN Panel'
admin.site.index_title = 'Welcome to MyBlog ADMIN'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='users/password_reset.html'),
         name='password-reset'
         ),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),

    path('profile/', user_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

