from django.urls import path
from .views import Home, HR, AIV, Canvas

app_name = "administrator"
urlpatterns = [
    path('', Home.as_view(), name="dashboard"),
    path('hr/', HR.as_view(), name="hr"),
    path('aiv/', AIV.as_view(), name="aiv"),
    path('canvas/', Canvas.as_view(), name="canvas")
]