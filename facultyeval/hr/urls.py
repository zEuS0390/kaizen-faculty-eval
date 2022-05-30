from django.urls import path
from .views import *

app_name = "hr"
urlpatterns = [
    path("", RedirectIndex.as_view(), name="redirect_index"),
    path("<slug:SEM>/<slug:SY>/update-hr-eval-scores/<int:ID>/export_pdf", GeneratePdf.as_view(), name='export_hr_pdf'),
    path("<slug:SEM>/<slug:SY>/update-hr-eval-scores/<int:ID>/export", export_hr_csv, name='export_hr_csv'),
    path("list-of-criteria/", ListOfCriteria.as_view(), name="list_of_criteria"),
    path("delete-criterion/<int:ID>/", DeleteHRCriterion, name="delete_hr_criterion"),
    path("<slug:SEM>/<slug:SY>/", Index.as_view(), name="index"),
    path("<slug:SEM>/<slug:SY>/delete-hr-rating/<int:ID>", DeleteHRRating, name="delete_hr_rating"),
    path("<slug:SEM>/<slug:SY>/hr-rating-entry/", HRRatingEntry.as_view(), name="hr_rating_entry"), # <- This might not be used anymore
    path("<slug:SEM>/<slug:SY>/new-hr-evaluation/<int:ID>", NewHREvaluation, name="new_hr_evaluation"),
    path("<slug:SEM>/<slug:SY>/update-hr-eval-scores/<int:ID>/", EvalScores.as_view(), name="update_hr_eval_scores"),
    path("<slug:SEM>/<slug:SY>/hr-eval-scores/criterion-scores/<int:ID>/<int:CRITERIONID>/", CriterionScores.as_view(), name="criterion_scores")
]