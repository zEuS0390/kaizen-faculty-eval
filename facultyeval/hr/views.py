from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .decorators import admin_only
from django.views import View
from accounts.models import Member
from django.contrib import messages
from .forms import *
from .models import *
from django.core.mail import EmailMessage


# Create your views here.
class Index(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY):
        members = Member.objects.all()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        context = {"hr_data": [], "SEM": SEM, "SY":SY}
        for member in members:
            result = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM)
            if result.exists():
                context["hr_data"].append([member, True])
                continue
            context["hr_data"].append([member, False])
        return render(request, template_name="hr/index.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY):
        return redirect("/")

class EvalScores(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY, ID):
        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating.objects.filter(member=member).first()
        hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating).all()
        context = {
            "hrcriterionscores": hrcriterionscores,
            "member_id": ID,
            "SY": SY,
            "SEM": SEM
        }
        return render(request, template_name="hr/updatehrevalscores.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY, ID):
        return redirect("/")

class CriterionScores(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY, ID):
        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating(member=member, school_year=school_year, semester=SEM)
        form = HRCriterionScoresForm({
            "hrrating": hrrating
        })
        return render(request, template_name="hr/criterionscores.html", context={"form": form})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY, ID):
        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating(member=member, school_year=school_year, semester=SEM)
        post = {"hrrating": [hrrating], **request.POST}
        form = HRCriterionScoresForm(post)
        print(post)
        if form.is_valid():
            hrcriterionscores = form.save(commit=False)
            hrrating = form.cleaned_data.get("hrrating")
            hrcriterion = form.cleaned_data.get("hrcriterion")
            if HRCriterionScores.objects.filter(hrrating=hrrating, 
                                                hrcriterion=hrcriterion).exists():
                messages.error(request, "This criterion score already exist!")
                return redirect("canvas:eval_entry")
            hrcriterionscores.save()
            messages.success(request, "Criterion score successfully created!")
            return redirect("hr:hr_eval_scores", SEM=SEM, SY=SY, ID=ID)
        messages.error(request, f"{form.errors}")
        return redirect("hr:criterion_scores", SEM=SEM, SY=SY, ID=ID)

@login_required(login_url="accounts:login")
@admin_only
def ListofCriteria(request):
    criteria = HRCriterion.objects.all()
    context = {
        "criteria": criteria
    }
    return render(request, template_name="hr/listofcriteria.html", context=context)

class HRRatingEntry(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY):
        form = HRRatingForm()
        context = {"form": form}
        return render(request, template_name="hr/hrrating.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY):
        form = HRRatingForm(request.POST)
        if form.is_valid():
            hrrating = form.save(commit=False)
            member = form.cleaned_data.get("member")
            semester = form.cleaned_data.get("semester")
            school_year = form.cleaned_data.get("school_year")
            if HRRating.objects.filter(member=member, semester=semester, school_year=school_year).exists():
                messages.error(request, "HR evaluation entry already exist!")
                return redirect("hr:hr_rating_entry", SEM=semester, SY=school_year)
            hrrating.save()
            messages.success(request, "HR evaluation entry successfully created!")
            return redirect("hr:index", SEM=semester, SY=school_year)
        return redirect("hr:hr_rating_entry", SEM=SEM, SY=SY)

@login_required(login_url="accounts:login")
@admin_only
def DeleteHRRating(request, SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM)
    if hrrating.exists():
        hrrating.delete()
        messages.success(request, "HR evaluation entry was successfully deleted!")
        return redirect("hr:index", SEM=SEM, SY=SY)
    else:
        messages.error(request, f"ID {ID} does not exist!")
    return redirect("hr:index", SEM=SEM, SY=SY)
