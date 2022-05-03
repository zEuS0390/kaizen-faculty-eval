from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from administrator.decorators import admin_only
from administrator.models import ActivityLogs
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