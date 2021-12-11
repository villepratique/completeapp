from django.urls import path , include
from .views import register , logout_request
from django.contrib.auth import views as auth_views

auth_views.PasswordResetView.template_name = "registration/auth/password_reset_form.html"


urlpatterns = [
    # path('login/', login , name="login"),
    path('inscription/', register , name="register"),
    path('deconnexion/', logout_request , name="logout_request"),

    #   path(
    #     'change-password/',
    #     auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    # ),
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset_complete.html'), name='password_change'),
    # path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/auth/password_change_done.html'), name='password_change_done'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/auth/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/auth/password_reset_complete.html'), name='password_reset_complete'),


]

#  path(
#         'change-password/',
#         auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
#     ),