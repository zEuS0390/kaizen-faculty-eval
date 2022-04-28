from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import EmailMessage

from .decorators import admin_only
from .forms import EvaluationForm
from administrator.models import SchoolYear, ActivityLogs
from .models import MGRating

# Create your views here.
class Index(View):
    """
    Index is the first view of the LMS (Canvas), it consist basic implementation 
    of CRUD for accessing the application's database.
    """

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, MG, SY):
        
        print(SEM, MG, SY)
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        ratings = MGRating.objects.filter(school_year=school_year, group_title=MG, semester=SEM)
        return render(request, template_name="canvas/index.html", context={"ratings": ratings})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")

class CreateEval(View):
    """
    This view will create a performance evaluation of LMS (Canvas)
    for a specified faculty member that exist within the database.
    """

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        form = EvaluationForm()
        return render(request, template_name="canvas/evaluation_form.html", context={"form": form})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        form = EvaluationForm(request.POST)
        if form.is_valid:
            mgrating = form.save(commit=False)
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
            logs = ActivityLogs(member=member, activity_log=ActivityLogs.ADDED, eval_log=ActivityLogs.LMS)
            logs.save()
            messages.success(request, "Evaluation successfully created!")
            msg = EmailMessage('New Evaluation', 'You have a new evaluation in {school_year} - {group_title} - {semester}. You may now view it in the Faculty Evaluation'.format(school_year=school_year, group_title=group_title, semester=semester), to=[member.user.email])
            msg.send()
            return redirect("canvas:index", SEM=semester, MG=group_title, SY=school_year)
        return redirect("/")

class EditEval(View):
    """
    This view will edit an existing performance evaluation
    of a specified faculty member using ID attribute in 
    LMS's (Canvas) MGRating table.
    """

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, ID):
        result = MGRating.objects.filter(id=ID)
        # Check if the performance evaluation already exist
        if result.exists():
            selected_mgrating = result.first()
            form = EvaluationForm({
                "member": selected_mgrating.member,
                "school_year": selected_mgrating.school_year,
                "group_title": selected_mgrating.group_title,
                "semester": selected_mgrating.semester,
                "part1": selected_mgrating.part1,
                "part2": selected_mgrating.part2,
                "final": selected_mgrating.final,
                "remarks": selected_mgrating.remarks
            })
            logs = ActivityLogs(member=selected_mgrating.member, activity_log=ActivityLogs.UPDATE, eval_log=ActivityLogs.LMS)
            logs.save()
            return render(request, template_name="canvas/evaluation_form.html", context={"form":form})
        messages.error(request, f"ID {ID} does not exist!")
        SEM = result.first().semester
        MG = result.first().group_title
        SY = result.first().school_year
        return redirect("canvas:index", SEM, MG, SY)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, ID):
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            selected_mgrating = MGRating.objects.filter(id=ID)
            selected_mgrating.update(**form.cleaned_data)
        SEM = form.cleaned_data.get("semester")
        MG = form.cleaned_data.get("group_title")
        SY = form.cleaned_data.get("school_year")
        return redirect("canvas:index", SEM, MG, SY)

@login_required(login_url="accounts:login")
@admin_only
def DeleteEval(request, ID):
    """
    This view will delete the performance evaluation of a specified
    faculty member using ID attribute in LMS's (Canvas) MGRating table.
    """
    result = MGRating.objects.filter(id=ID)
    SEM = result.first().semester
    MG = result.first().group_title
    SY = result.first().school_year
    # Check if the performance evaluation already exist
    if result.exists():
        logs = ActivityLogs(member=result.first().member, activity_log=ActivityLogs.DELETED, eval_log=ActivityLogs.LMS)
        logs.save()
        result.delete()
        messages.success(request, f"ID {ID} has been successfully removed")
        return redirect("canvas:index", SEM, MG, SY)
    messages.error(request, f"ID {ID} does not exist!")
    return redirect("canvas:index", SEM, MG, SY)
    
