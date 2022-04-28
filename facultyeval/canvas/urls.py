from django.urls import path
from .views import *

app_name = "canvas"
urlpatterns = [
    path("<slug:SEM>/<str:MG>/<slug:SY>/", Index.as_view(), name="index"),
    path("evaluation-form-entry/", CreateEval.as_view(), name="eval_entry"),
    path("edit-evaluation/<int:ID>/", EditEval.as_view(), name="edit_eval"),
    path("delete-evaluation/<int:ID>/", DeleteEval, name="delete_eval")
]