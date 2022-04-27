from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from administrator.decorators import admin_only
from canvas.models import Member

# Create your views here.
class Dashboard(View):
    
    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        return render(request, template_name="administrator/dashboard.html", context={})

class HR(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        return render(request, template_name="administrator/hr.html", context={})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return 

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