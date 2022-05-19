from django.urls import path
from .views import *

app_name = "aiv"
urlpatterns = [
    path("<slug:SEM>/<slug:SY>/", Index.as_view(), name="index"),
    path("list-of-criteria/", ListofCriteria, name="list_of_criteria"),
    path("<slug:SEM>/<slug:SY>/delete-aiv-rating/<int:ID>", DeleteAIVRating, name="delete_aiv_rating"),
    path("<slug:SEM>/<slug:SY>/aiv-rating-entry/", AIVRatingEntry.as_view(), name="aiv_rating_entry"),
    path("<slug:SEM>/<slug:SY>/update-aiv-eval-scores/<int:ID>/", EvalScores.as_view(), name="update_aiv_eval_scores"),
    path("<slug:SEM>/<slug:SY>/aiv-eval-scores/criterion-scores/<int:ID>/<int:CRITERIONID>/", CriterionScores.as_view(), name="criterion_scores")
]