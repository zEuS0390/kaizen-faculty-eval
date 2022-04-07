from django.urls import path
from .views import Dashboard, HR, AIV

app_name = "administrator"
urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('hr/', HR.as_view(), name="hr"),
    path('aiv/', AIV.as_view(), name="aiv"),
]