from django.urls import path
from .views import *

app_name = "aiv"
urlpatterns = [
    path("", RedirectIndex.as_view(), name="redirect_index"),
    path("<slug:SEM>/<slug:SY>/update-aiv-eval-scores/<int:ID>/export_pdf", GeneratePdf.as_view(), name='export_aiv_pdf'),
    path("<slug:SEM>/<slug:SY>/update-aiv-eval-scores/<int:ID>/export", export_aiv_csv, name='export_aiv_csv'),
    path("list-of-criteria/", ListOfCriteria.as_view(), name="list_of_criteria"),
    path("delete-criterion/<int:ID>/", DeleteAIVCriterion, name="delete_aiv_criterion"),
    path("<slug:SEM>/<slug:SY>/", Index.as_view(), name="index"),
    path("<slug:SEM>/<slug:SY>/delete-aiv-rating/<int:ID>", DeleteAIVRating, name="delete_aiv_rating"),
    path("<slug:SEM>/<slug:SY>/aiv-rating-entry/", AIVRatingEntry.as_view(), name="aiv_rating_entry"),
    path("<slug:SEM>/<slug:SY>/update-aiv-eval-scores/<int:ID>/", EvalScores.as_view(), name="update_aiv_eval_scores"),
    path("<slug:SEM>/<slug:SY>/new-aiv-evaluation/<int:ID>", NewAIVEvaluation, name="new_aiv_evaluation"),
    path("<slug:SEM>/<slug:SY>/aiv-eval-scores/criterion-scores/<int:ID>/<int:CRITERIONID>/", CriterionScores.as_view(), name="criterion_scores")
]