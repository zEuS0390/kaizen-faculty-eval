from django.urls import path
from .views import *

app_name = "member"
urlpatterns = [
    path("", Home, name="home"),
    path("profile/", Profile, name="profile"),
    path("hr/", HR, name="hr"),
    path("hr/eval-scores/<slug:SEM>/<slug:SY>/", HREvalScores, name="hr_eval_scores"),
    path("aiv/", AIV, name="aiv"),
    path("aiv/eval-scores/<slug:SEM>/<slug:SY>", AIVEvalScores, name="aiv_eval_scores"),
    path("lms/", LMS, name="lms"),
    path("about/", About, name="about")
]