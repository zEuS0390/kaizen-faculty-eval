from django.urls import path, reverse_lazy
from .views import Login, Register, logoutUser, PassResetView
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", Register.as_view(), name="register"),
    path("password-reset/", 
        PassResetView.as_view(
            template_name="accounts/reset_password.html",
            success_url=reverse_lazy("accounts:password_reset_done"),
            email_template_name="accounts/password_reset.txt"),
        name="password_reset"
    ),
    path("password-reset-done/", 
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/reset_password_done.html"), 
        name="password_reset_done"
    ),
    path("password-reset-confirm/<uidb64>/<token>/", 
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/reset_password_confirm.html", 
            success_url=reverse_lazy("accounts:password_reset_complete")),
        name="password_reset_confirm"
    ),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"), name="password_reset_complete"),
]