from django.urls import path
from .views import *

app_name = "canvas"
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("evaluation-form-entry/", EvaluationFormEntry.as_view(), name="eval_entry"),
    path("delete-evaluation/<int:ID>/", DeleteEval, name="delete_eval")
]