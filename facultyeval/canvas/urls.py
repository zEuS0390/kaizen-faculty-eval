from django.urls import path
from .views import *

app_name = "canvas"
urlpatterns = [
    path("", RedirectIndex.as_view(), name="redirect_index"),
    path("<slug:SEM>/<str:MG>/<slug:SY>/export_pdf", GeneratePdf.as_view(), name='export_lms_pdf'),
    path("<slug:SEM>/<str:MG>/<slug:SY>/export", export_lms_csv, name='export_lms_csv'),
    path("<slug:SEM>/<str:MG>/<slug:SY>/", Index.as_view(), name="index"),
    path("evaluation-form-entry/", CreateEval.as_view(), name="eval_entry"),
    path("edit-evaluation/<int:ID>/", EditEval.as_view(), name="edit_eval"),
    path("delete-evaluation/<int:ID>/", DeleteEval, name="delete_eval")
]