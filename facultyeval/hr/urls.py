from django.urls import path
from .views import *

app_name = "hr"
urlpatterns = [
    path("list-of-criteria/", ListofCriteria, name="list_of_criteria"),
    path("<slug:SEM>/<slug:SY>/", Index.as_view(), name="index"),
    path("<slug:SEM>/<slug:SY>/hr-eval-scores/<int:ID>/", EvalScores.as_view(), name="hr_eval_scores"),
    path("<slug:SEM>/<slug:SY>/hr-eval-scores/criterion-scores/<int:ID>/", CriterionScores.as_view(), name="criterion_scores")
]