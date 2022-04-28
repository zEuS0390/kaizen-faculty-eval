from django.urls import path
from .views import *

app_name = "hr"
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("evaluation-form-entry/", CreateEval.as_view(), name="eval_entry")
]