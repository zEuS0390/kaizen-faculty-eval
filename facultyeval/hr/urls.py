from django.urls import path
from .views import *

app_name = "hr"
urlpatterns = [
    path("", Index.as_view(), name="index")
]