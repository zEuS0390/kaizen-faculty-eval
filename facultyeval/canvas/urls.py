from django.urls import path
from .views import Index

app_name = "canvas"
urlpatterns = [
    path("", Index.as_view(), name="index")
]