from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from administrator.decorators import admin_only
from administrator.models import ActivityLogs, SchoolYear
from canvas.models import Member
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
import csv

# Create your views here.
class Dashboard(View):
    
    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        logs = ActivityLogs.objects.all()
        return render(request, template_name="administrator/dashboard.html", context={"logs": logs})

class AIV(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        return render(request, template_name="administrator/aiv.html", context={})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")

@login_required(login_url="accounts:login")
@admin_only
def About(request):
    return render(request, template_name="administrator/about.html", context={})

@login_required(login_url="accounts:login")
@admin_only
def ListOfMembers(request):
    members = Member.objects.all()
    return render(request, template_name="administrator/listofmembers.html", context={"members": members})

@login_required(login_url="accounts:login")
@admin_only
def Profile(request):
    return render(request, template_name="administrator/profile.html", context={})

@login_required(login_url="accounts:login")
@admin_only
def DeleteMember(request, ID):
    member = Member.objects.filter(id=ID)
    if member.exists():
        member.first().user.delete()
    return redirect("administrator:list_of_members")

@login_required(login_url="accounts:login")
@admin_only
def ViewMemberProfile(request, ID):
    member = Member.objects.filter(id=ID)
    if member.exists():
        cntx_user = member.first().user
        return render(request, template_name="administrator/viewmemberprofile.html", context={"cntx_user": cntx_user})
    return redirect("/")

class SchoolYearView(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        school_years = SchoolYear.objects.all()
        return render(request, template_name="administrator/schoolyear.html", context={"data": school_years})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return

class NewSchoolYear(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        form = SchoolYearForm()
        context = {
            "form": form
        }
        return render(request, template_name="administrator/schoolyearform.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        form = SchoolYearForm(request.POST)
        if form.is_valid():
            SY = form.save(commit=False)
            school_year = form.cleaned_data.get("school_year")
            if SchoolYear.objects.filter(school_year=school_year).exists():
                messages.error(request, "School year already exist!")
                return redirect("administrator:new_school_year")
            SY.save()
            messages.success(request, "School year has successfully added!")
            return redirect("administrator:school_year")
        messages.error(request, "Invalid input!")
        return redirect("administrator:new_school_year")

@login_required(login_url="accounts:login")
@admin_only
def DeleteSchoolYear(request, ID):
    school_year = SchoolYear.objects.filter(id=ID)
    if school_year.exists():
        school_year.delete()
        messages.success(request, "School year has successfully deleted!")
    else:
        messages.error(request, "Error encountered deleting the school year")
    return redirect("administrator:school_year")

@login_required(login_url="accounts:login")
@admin_only
def export_members_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registered_faculty_members.csv"'
    writer = csv.writer(response)
    writer.writerow(["List of Registered Faculty Members"])
    members = Member.objects.all()
    for member in members:
        writer.writerow([member])
    return response