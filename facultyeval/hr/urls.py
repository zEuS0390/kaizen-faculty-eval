from django.urls import path
from .views import *

app_name = "hr"
urlpatterns = [
    path("list-of-criteria/", ListofCriteria, name="list_of_criteria"),
    path("<slug:SEM>/<slug:SY>/", Index.as_view(), name="index"),
    path("<slug:SEM>/<slug:SY>/delete-hr-rating/<int:ID>", DeleteHRRating, name="delete_hr_rating"),
    path("<slug:SEM>/<slug:SY>/hr-rating-entry/", HRRatingEntry.as_view(), name="hr_rating_entry"),
    path("<slug:SEM>/<slug:SY>/update-hr-eval-scores/<int:ID>/", EvalScores.as_view(), name="update_hr_eval_scores"),
    path("<slug:SEM>/<slug:SY>/hr-eval-scores/criterion-scores/<int:ID>/<int:CRITERIONID>/", CriterionScores.as_view(), name="criterion_scores")
]