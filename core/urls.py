from typing import Any, Dict, Optional
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.template import loader
from django.urls import path , include

from .sendMailJet import executeSendMail
from .views import register , logout_request
from django.contrib.auth import views as auth_views

from django.core.mail.backends.smtp import EmailBackend


class CustomPasswordResetForm(PasswordResetForm):
    
    def send_mail(self, subject_template_name: str, 
    email_template_name: str, 
    context: Dict[str, Any], 
    from_email: Optional[str], 
    to_email: str, 
    html_email_template_name: Optional[str] = ...) -> None:
        body = loader.render_to_string(email_template_name, context)
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        executeSendMail(subject ,from_email,to_email , body)
        return 


class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = CustomPasswordResetForm
    from_email = "richard.bathiebo.7@gmail.com"
    template_name = "registration/auth/password_reset_form.html"
    email_template_name = 'registration/auth/password_reset_emailR.html'

urlpatterns = [
    # path('login/', login , name="login"),
    
    # path('translation/', translate_view , name="translate_view"),
    path('inscription/', register , name="register"),
    path('deconnexion/', logout_request , name="logout_request"),

    #   path(
    #     'change-password/',
    #     auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    # ),
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset_complete.html'), name='password_change'),
    # path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/auth/password_change_done.html'), name='password_change_done'),

    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/auth/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/auth/password_reset_complete.html'), name='password_reset_complete'),


]

#  path(
#         'change-password/',
#         auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
#     ),