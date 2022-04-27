from django.urls import path
from .views import *

app_name = "administrator"
urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('hr/', HR.as_view(), name="hr"),
    path('aiv/', AIV.as_view(), name="aiv"),
    path('about/', About, name="about"),
    path('list_of_members/', ListOfMembers, name="list_of_members")
]