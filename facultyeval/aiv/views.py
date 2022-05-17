from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from accounts.models import Member
from administrator.models import SchoolYear
from hr.models import HRRating
from .decorators import *

# Create your views here.
class Index(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY):
        members = Member.objects.all()
        context = {"aiv_data": [], "SEM": SEM, "SY":SY}
        for member in members:
            context["aiv_data"].append([member, False])
        return render(request, template_name="aiv/index.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY):
        return redirect("/")