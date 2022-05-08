from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from administrator.decorators import admin_only
from administrator.models import ActivityLogs, SchoolYear
from canvas.models import Member

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