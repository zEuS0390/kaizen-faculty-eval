from django.urls import path
from .views import *

app_name = "administrator"
urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('aiv/', AIV.as_view(), name="aiv"),
    path('about/', About, name="about"),
    path('list_of_members/', ListOfMembers, name="list_of_members"),
    path('profile/', Profile, name="profile"),
    path('delete-member/<int:ID>/', DeleteMember, name="delete_member"),
    path("view-profile-member/<int:ID>/", ViewMemberProfile, name="view_profile_member"),
    path("school-year/", SchoolYearView.as_view(), name="school_year"),
    path("school-year/delete/<int:ID>/", DeleteSchoolYear, name="delete_school_year"),
    path("school-year/new/", NewSchoolYear.as_view(), name="new_school_year")
]