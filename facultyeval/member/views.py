from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import member_only
from administrator.models import ActivityLogs
from accounts.models import Member

# Create your views here.
@login_required(login_url="accounts:login")
@member_only
def Home(request):
    member = Member.objects.filter(user=request.user).first()
    logs = ActivityLogs.objects.filter(member=member)
    return render(request, template_name="member/home.html", context={"logs":logs})

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

@login_required(login_url="accounts:login")
@member_only
def About(request):
    return render(request, template_name="member/about.html", context={})