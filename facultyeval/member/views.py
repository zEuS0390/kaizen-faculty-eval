from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import member_only

# Create your views here.
@login_required(login_url="accounts:login")
@member_only
def Home(request):
    return render(request, template_name="member/home.html", context={})

@login_required(login_url="accounts:login")
@member_only
def Profile(request):
    return render(request, template_name="member/profile.html", context={})

@login_required(login_url="accounts:login")
@member_only
def HR(request):
    return render(request, template_name="member/hr.html", context={})

@login_required(login_url="accounts:login")
@member_only
def AIV(request):
    return render(request, template_name="member/aiv.html", context={})

@login_required(login_url="accounts:login")
@member_only
def LMS(request):
    return render(request, template_name="member/lms.html", context={})