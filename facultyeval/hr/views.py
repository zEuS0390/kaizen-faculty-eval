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
        if not school_year is None:
            for member in members:
                result = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM)
                if result.exists():
                    context["hr_data"].append([member, True])
                    continue
                context["hr_data"].append([member, False])
        return render(request, template_name="hr/index.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY,):
        return redirect("/")

class EvalScores(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY, ID):
        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating.objects.filter(member=member)
        if not hrrating.exists():
            hrrating_new = HRRating(member=member, school_year=school_year, semester=SEM)
            hrrating_new.save()
        hrrating = HRRating.objects.filter(member=member).first()
        hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating).all()
        context = {
            "hrcriterionscores": hrcriterionscores,
            "member_id": ID,
            "SY": SY,
            "SEM": SEM
        }
        return render(request, template_name="hr/hrevalscores.html", context=context)

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