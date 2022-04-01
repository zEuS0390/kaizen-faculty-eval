from django.urls import path
from .views import Index
from django.conf import settings
from django.conf.urls.static import static

app_name = "canvas"
urlpatterns = [
    path("", Index.as_view(), name="index")
]