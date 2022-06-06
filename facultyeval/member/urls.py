from django.urls import path
from .views import *

app_name = "member"
urlpatterns = [
    path("", Home, name="home"),
    path("profile/", Profile, name="profile"),
    path("profile/edit/", EditProfile.as_view(), name="edit_profile"),
    path("hr/", HR, name="hr"),
    path("hr/eval-scores/<slug:SEM>/<slug:SY>/", HREvalScores, name="hr_eval_scores"),
    path("aiv/", AIV, name="aiv"),
    path("aiv/eval-scores/<slug:SEM>/<slug:SY>", AIVEvalScores, name="aiv_eval_scores"),
    path("lms/<slug:SEM>/<slug:SY>/", LMS, name="lms"),
    path("lms/", RedirectLMS, name="redirect_lms"),
    path("about/", About, name="about"),
    path("hr/eval-scores/<slug:SEM>/<slug:SY>/export_pdf", GeneratePdfHR.as_view(), name='export_hr_pdf'),
    path("hr/eval-scores/<slug:SEM>/<slug:SY>/export", export_hr_csv, name='export_hr_csv'),
    path("aiv/eval-scores/<slug:SEM>/<slug:SY>/export_pdf", GeneratePdfAIV.as_view(), name='export_aiv_pdf'),
    path("aiv/eval-scores/<slug:SEM>/<slug:SY>/export", export_aiv_csv, name='export_aiv_csv')
]