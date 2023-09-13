from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
#from blogapp import views

urlpatterns = [
    path('signup',views.userview,name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('forget_password',auth_view.PasswordResetView.as_view(template_name='password_reset.html',html_email_template_name='password_reset_email.html'),name='forget_password'),
    path('password_reset_done',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('profile',views.profile,name='profile')


]
