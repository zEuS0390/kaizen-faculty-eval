from django.urls import path
from .views import *

app_name = "member"
urlpatterns = [
    path("", Profile.as_view(), name="profile")
]