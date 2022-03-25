from django.urls import path
from .views import Login, Register, logoutUser, Landing

app_name = "accounts"
urlpatterns = [
    path("", Landing.as_view(), name="landing"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", Register.as_view(), name="register")
]