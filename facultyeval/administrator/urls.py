from django.urls import path
from .views import Dashboard, AIV, About

app_name = "administrator"
urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('aiv/', AIV.as_view(), name="aiv"),
    path('about/', About, name="about")
]