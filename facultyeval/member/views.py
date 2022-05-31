from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import member_only
from administrator.models import ActivityLogs
from accounts.models import Member
from hr.models import *
from aiv.models import *

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
    member = Member.objects.filter(user=request.user).first()
    hrratings = HRRating.objects.filter(member=member).all()
    context = {
        "hrratings": hrratings
    }
    return render(request, template_name="member/hr.html", context=context)

@login_required(login_url="accounts:login")
@member_only
def HREvalScores(request, SEM, SY):
    member = Member.objects.filter(user=request.user).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
    hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating).all()
    context = {
            "hrcriterionscores": hrcriterionscores,
            "SY": SY,
            "SEM": SEM
    }
    return render(request, template_name="member/hrevalscores.html", context=context)

@login_required(login_url="accounts:login")
@member_only
def AIV(request):
    member = Member.objects.filter(user=request.user).first()
    aivratings = AIVRating.objects.filter(member=member).all()
    context = {
        "aivratings": aivratings
    }
    return render(request, template_name="member/aiv.html", context=context)

@login_required(login_url="accounts:login")
@member_only
def AIVEvalScores(request, SEM, SY):
    member = Member.objects.filter(user=request.user).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
    aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating).all()
    context = {
            "aivcriterionscores": aivcriterionscores,
            "SY": SY,
            "SEM": SEM
    }
    return render(request, template_name="member/aivevalscores.html", context=context)

@login_required(login_url="accounts:login")
@member_only
def LMS(request):
    return render(request, template_name="member/lms.html", context={})

@login_required(login_url="accounts:login")
@member_only
def About(request):
    return render(request, template_name="member/about.html", context={})