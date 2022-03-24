from django.urls import path
from .views import Login, Register, logoutUser

app_name = "accounts"
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", logoutUser, name="logout"),
    path("reigster/", Register.as_view(), name="register")
]