from django.urls import path
from .views import *

app_name = "aiv"
urlpatterns = [
    path("<slug:SEM>/<slug:SY>/", Index.as_view(), name="index")
]