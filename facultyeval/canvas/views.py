from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import admin_only
from .forms import CreateEvaulation
from administrator.models import SchoolYear
from .models import MGRating

# Create your views here.
class Index(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        school_year = SchoolYear.objects.get(school_year="2021-2022")
        ratings = MGRating.objects.filter(school_year=school_year, group_title="MG1", semester="1st Sem")
        return render(request, template_name="canvas/index.html", context={"ratings": ratings})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")

class EvaluationFormEntry(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        form = CreateEvaulation()
        return render(request, template_name="canvas/evaluation_form_entry.html", context={"form": form})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        form = CreateEvaulation(request.POST)
        if form.is_valid:
            mgrating = form.save(commit=False)
            # Check if the evaluation form entry already exist
            member = form.cleaned_data.get("member")
            school_year = form.cleaned_data.get("school_year")
            group_title = form.cleaned_data.get("group_title")
            semester = form.cleaned_data.get("semester")
            if MGRating.objects.filter(member=member, 
                                       school_year=school_year, 
                                       group_title=group_title, 
                                       semester=semester).exists():
                messages.error(request, "Evaluation form entry already exist!")
                return redirect("canvas:eval_entry")
            mgrating.save()
            return redirect("canvas:index")
        return redirect("/")

@login_required(login_url="accounts:login")
@admin_only
def DeleteEval(request, ID):
    MGRating.objects.filter(id=ID).delete()
    return redirect("canvas:index")