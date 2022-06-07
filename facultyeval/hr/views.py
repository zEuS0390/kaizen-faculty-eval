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
from administrator.models import ActivityLogs
from django.http import HttpResponse
import csv
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import View
from django.template.loader import render_to_string
from django.conf import settings
import os

class RedirectIndex(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        SEM = "1st-Sem"
        try:
            _SY = SchoolYear.objects.latest("id")
            SY = _SY.school_year
            return redirect("hr:index", SEM=SEM, SY=SY)
        except:
            pass
        messages.error(request, "School year does not exist!")
        return redirect("administrator:dashboard")

# Create your views here.
class Index(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY):
        members = Member.objects.all()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        sy_group = SchoolYear.objects.all()
        form = HRRatingForm()
        context = {"hr_data": [], "SEM": SEM, "SY":SY, "sy_group": sy_group, "form": form}
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
            criteria = HRCriterion.objects.all()
            for criterion in criteria:
                criterion_scores = HRCriterionScores(hrrating=hrrating, hrcriterion=criterion)
                criterion_scores.save()
            messages.success(request, "HR evaluation entry successfully created!")
            #ActivityLogs
            logs = ActivityLogs(member=member, activity_log=ActivityLogs.ADDED, eval_log=ActivityLogs.HR)
            logs.save()
            #End of ActivityLogs
            return redirect("hr:index", SEM=semester, SY=school_year)
        return redirect("hr:hr_rating_entry", SEM=SEM, SY=SY)

@login_required(login_url="accounts:login")
@admin_only
def NewHREvaluation(request, SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    if HRRating.objects.filter(member=member, semester=SEM, school_year=school_year).exists():
        messages.error(request, "HR evaluation entry already exist!")
        return redirect("hr:index", SEM=SEM, SY=school_year)
    hrrating = HRRating(member=member, semester=SEM, school_year=school_year)
    hrrating.save()
    criteria = HRCriterion.objects.all()
    for criterion in criteria:
        criterion_scores = HRCriterionScores(hrrating=hrrating, hrcriterion=criterion)
        criterion_scores.save()
    messages.success(request, "HR evaluation entry successfully created!")
    #ActivityLogs
    logs = ActivityLogs(member=member, activity_log=ActivityLogs.ADDED, eval_log=ActivityLogs.HR)
    logs.save()
    #End of ActivityLogs
    return redirect("hr:index", SEM=SEM, SY=SY)

class EvalScores(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY, ID):
        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
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
    def get(self, request, SEM, SY, ID, CRITERIONID):
        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        hrcriterion = HRCriterion.objects.filter(id=CRITERIONID).first()
        hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating, hrcriterion=hrcriterion)
        if hrcriterionscores.exists():
            result = hrcriterionscores.first()
            form = HRCriterionScoresForm(initial={
                "program_chair_score": result.program_chair_score,
                "student_score": result.student_score,
                "average_score": result.average_score,
                "remarks": result.remarks
            })
        else:
            form = HRCriterionScoresForm()
        return render(request, template_name="hr/criterionscores.html", context={"form": form})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY, ID, CRITERIONID):
        form = HRCriterionScoresForm(request.POST)
        if form.is_valid():
            member = Member.objects.filter(id=ID).first()
            school_year = SchoolYear.objects.filter(school_year=SY).first()
            hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
            hrcriterion = HRCriterion.objects.filter(id=CRITERIONID).first()
            hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating, hrcriterion=hrcriterion)
            hrcriterionscores.update(**form.cleaned_data)
            messages.success(request, "Successfully updated criterion scores!")
        else:
            messages.error(request, "Error encountered updating criterion scores!")
        return redirect("hr:update_hr_eval_scores", SEM=SEM, SY=SY, ID=ID)

class ListOfCriteria(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        criteria = HRCriterion.objects.all()
        form = HRCriterionForm()
        context = {
            "criteria": criteria,
            "form": form
        }
        return render(request, template_name="hr/listofcriteria.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        # New criterion form
        if 'new_criterion' in request.POST:
            form = HRCriterionForm(request.POST)
            if form.is_valid():
                hrcriterion = form.save(commit=False)
                title = form.cleaned_data.get('title')
                if HRCriterion.objects.filter(title=title).exists():
                    messages.error(request, "HR evaluation criterion already exist!")
                    return redirect("hr:list_of_criteria")
                hrcriterion.save()
                messages.success(request, "HR evaluation criterion successfully created!")
                return redirect("hr:list_of_criteria")
        return redirect("/")

@login_required(login_url="accounts:login")
@admin_only
def DeleteHRCriterion(request, ID):
    hrcriterion = HRCriterion.objects.filter(id=ID)
    if hrcriterion.exists():
        hrcriterion.delete()
        messages.success(request, "HR evaluation criterion was successfully deleted!")
        return redirect("hr:list_of_criteria")
    else:
        messages.error(request, f"ID {ID} does not exist!")
    return redirect("hr:list_of_criteria")

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
            criteria = HRCriterion.objects.all()
            for criterion in criteria:
                criterion_scores = HRCriterionScores(hrrating=hrrating, hrcriterion=criterion)
                criterion_scores.save()
            messages.success(request, "HR evaluation entry successfully created!")
            #ActivityLogs
            logs = ActivityLogs(member=member, activity_log=ActivityLogs.ADDED, eval_log=ActivityLogs.HR)
            logs.save()
            #End of ActivityLogs
            return redirect("hr:index", SEM=semester, SY=school_year)
        return redirect("hr:hr_rating_entry", SEM=SEM, SY=SY)

@login_required(login_url="accounts:login")
@admin_only
def DeleteHRRating(request, SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM)
    if hrrating.exists():
        #ActivityLogs
        logs = ActivityLogs(member=member, activity_log=ActivityLogs.DELETED, eval_log=ActivityLogs.HR)
        logs.save()
        #End of ActivityLogs
        hrrating.delete()
        messages.success(request, "HR evaluation entry was successfully deleted!")
        return redirect("hr:index", SEM=SEM, SY=SY)
    else:
        messages.error(request, f"ID {ID} does not exist!")
    return redirect("hr:index", SEM=SEM, SY=SY)


@login_required(login_url="accounts:login")
@admin_only
def export_hr_csv(request,SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hr_{}_{}_{}.csv"'.format(SEM, SY, member)
    writer = csv.writer(response)
    writer.writerow(["Faculty Member",member])
    writer.writerow(["Criterion", "Program Chair", "Student", "Average", "Remarks"])
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
    hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating)
    for item in hrcriterionscores:
        writer.writerow([item.hrcriterion,item.program_chair_score,item.student_score,item.average_score,item.remarks])
    return response 

def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

class GeneratePdf(View):
    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY, ID):

        member = Member.objects.filter(id=ID).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating).all()
        
        value = settings.BASE_DIR
        temp = os.path.join(value, "hr", "templates", "hr", "temp.html")
        open(temp, "w").write(render_to_string('hr/updatehrevalscores_temp.html', 
        {"hrcriterionscores": hrcriterionscores, "member": member, "SY": SY, "SEM": SEM}))
         
        # getting the template
        pdf = html_to_pdf('hr/temp.html')
         
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')