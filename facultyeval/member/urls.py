from django.urls import path
from .views import *

app_name = "member"
urlpatterns = [
    path("", Home, name="home"),
    path("profile/", Profile, name="profile"),
    path("hr/", HR, name="hr"),
    path("aiv/", AIV, name="aiv"),
    path("lms/", LMS, name="lms")
]