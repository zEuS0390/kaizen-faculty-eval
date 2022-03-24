from django.urls import path
from .views import Home

app_name = "administrator"
urlpatterns = [
    path('', Home.as_view(), name="dashboard")
]