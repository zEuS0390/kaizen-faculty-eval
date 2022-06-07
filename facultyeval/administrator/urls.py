from django.urls import path
from .views import *

app_name = "administrator"
urlpatterns = [
    path('list_of_members/export_pdf/', GeneratePdf.as_view(), name="export_members_pdf"), 
    # path("list_of_members/export_pdf", export_members_pdf, name='export_members_pdf'),
    path("list_of_members/export", export_members_csv, name='export_members_csv'),
    path('', Dashboard.as_view(), name="dashboard"),
    path('about/', About, name="about"),
    path('list_of_members/', ListOfMembers, name="list_of_members"),
    path('profile/', Profile, name="profile"),
    path("profile/edit/", EditProfile.as_view(), name="edit_profile"),
    path('delete-member/<int:ID>/', DeleteMember, name="delete_member"),
    path("view-profile-member/<int:ID>/", ViewMemberProfile, name="view_profile_member"),
    path("school-year/", SchoolYearView.as_view(), name="school_year"),
    path("school-year/delete/<int:ID>/", DeleteSchoolYear, name="delete_school_year"),
    path("school-year/new/", NewSchoolYear.as_view(), name="new_school_year")
]