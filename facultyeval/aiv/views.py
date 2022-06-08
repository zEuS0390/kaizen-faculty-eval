from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from accounts.models import Member
from django.contrib import messages
from .models import *
from .decorators import *
from .forms import *
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
            return redirect("aiv:index", SEM=SEM, SY=SY)
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
        context = {"aiv_data": [], "SEM": SEM, "SY":SY, "sy_group": sy_group}
        for member in members:
            result = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM)
            if result.exists():
                context["aiv_data"].append([member, True])
                continue
            context["aiv_data"].append([member, False])
        return render(request, template_name="aiv/index.html", context=context)

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
        aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating).all()
        context = {
            "aivcriterionscores": aivcriterionscores,
            "member_id": ID,
            "SY": SY,
            "SEM": SEM
        }
        return render(request, template_name="aiv/updateaivevalscores.html", context=context)

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
        aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        aivcriterion = AIVCriterion.objects.filter(id=CRITERIONID).first()
        aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating, aivcriterion=aivcriterion)
        if aivcriterionscores.exists():
            result = aivcriterionscores.first()
            form = AIVCriterionScoresForm(initial={
                "first_visit": result.first_visit,
                "second_visit": result.second_visit,
                "average_score": result.average_score,
                "remarks": result.remarks
            })
        else:
            form = AIVCriterionScoresForm()
        return render(request, template_name="aiv/criterionscores.html", context={"form": form})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY, ID, CRITERIONID):
        form = AIVCriterionScoresForm(request.POST)
        if form.is_valid():
            member = Member.objects.filter(id=ID).first()
            school_year = SchoolYear.objects.filter(school_year=SY).first()
            aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
            aivcriterion = AIVCriterion.objects.filter(id=CRITERIONID).first()
            aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating, aivcriterion=aivcriterion)
            aivcriterionscores.update(**form.cleaned_data)
            messages.success(request, "Successfully updated criterion scores!")
        else:
            messages.error(request, "Error encountered updating criterion scores!")
        return redirect("aiv:update_aiv_eval_scores", SEM=SEM, SY=SY, ID=ID)

class ListOfCriteria(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        criteria = AIVCriterion.objects.all()
        form = AIVCriterionForm()
        context = {
            "criteria": criteria,
            "form": form
        }
        return render(request, template_name="aiv/listofcriteria.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        # New criterion form
        if 'new_criterion' in request.POST:
            form = AIVCriterionForm(request.POST)
            if form.is_valid():
                aivcriterion = form.save(commit=False)
                title = form.cleaned_data.get('title')
                if AIVCriterion.objects.filter(title=title).exists():
                    messages.error(request, "AIV evaluation criterion already exist!")
                    return redirect("aiv:list_of_criteria")
                aivcriterion.save()
                messages.success(request, "AIV evaluation criterion successfully created!")
                return redirect("aiv:list_of_criteria")
        return redirect("/")

@login_required(login_url="accounts:login")
@admin_only
def DeleteAIVCriterion(request, ID):
    aivcriterion = AIVCriterion.objects.filter(id=ID)
    if aivcriterion.exists():
        aivcriterion.delete()
        messages.success(request, "AIV evaluation criterion was successfully deleted!")
        return redirect("aiv:list_of_criteria")
    else:
        messages.error(request, f"ID {ID} does not exist!")
    return redirect("aiv:list_of_criteria")

class AIVRatingEntry(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, SEM, SY):
        form = AIVRatingForm()
        context = {"form": form}
        return render(request, template_name="aiv/aivrating.html", context=context)
    
    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request, SEM, SY):
        form = AIVRatingForm(request.POST)
        if form.is_valid():
            aivrating = form.save(commit=False)
            member = form.cleaned_data.get("member")
            semester = form.cleaned_data.get("semester")
            school_year = form.cleaned_data.get("school_year")
            if AIVRating.objects.filter(member=member, semester=semester, school_year=school_year).exists():
                messages.error(request, "AIV evaluation entry already exist!")
                return redirect("aiv:aiv_rating_entry", SEM=semester, SY=school_year)
            aivrating.save()
            criteria = AIVCriterion.objects.all()
            for criterion in criteria:
                criterion_scores = AIVCriterionScores(aivrating=aivrating, aivcriterion=criterion)
                criterion_scores.save()
            messages.success(request, "AIV evaluation entry successfully created!")
            return redirect("aiv:index", SEM=semester, SY=school_year)
        return redirect("aiv:aiv_rating_entry", SEM=SEM, SY=SY)

@login_required(login_url="accounts:login")
@admin_only
def DeleteAIVRating(request, SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM)
    if aivrating.exists():
        aivrating.delete()
        messages.success(request, "AIV evaluation entry was successfully deleted!")
        #ActivityLogs
        logs = ActivityLogs(member=member, activity_log=ActivityLogs.DELETED, eval_log=ActivityLogs.AIV)
        logs.save()
        # End of ActivityLogs
        return redirect("aiv:index", SEM=SEM, SY=SY)
    else:
        messages.error(request, f"ID {ID} does not exist!")
    return redirect("aiv:index", SEM=SEM, SY=SY)

@login_required(login_url="accounts:login")
@admin_only
def NewAIVEvaluation(request, SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    if AIVRating.objects.filter(member=member, semester=SEM, school_year=school_year).exists():
        messages.error(request, "AIV evaluation entry already exist!")
        return redirect("aiv:index", SEM=SEM, SY=school_year)
    aivrating = AIVRating(member=member, semester=SEM, school_year=school_year)
    aivrating.save()
    criteria = AIVCriterion.objects.all()
    for criterion in criteria:
        criterion_scores = AIVCriterionScores(aivrating=aivrating, aivcriterion=criterion)
        criterion_scores.save()
    messages.success(request, "AIV evaluation entry successfully created!")
    #ActivityLogs
    logs = ActivityLogs(member=member, activity_log=ActivityLogs.ADDED, eval_log=ActivityLogs.AIV)
    logs.save()
    #End of ActivityLogs
    return redirect("aiv:index", SEM=SEM, SY=SY)

#CSV
@login_required(login_url="accounts:login")
@admin_only
def export_aiv_csv(request,SEM, SY, ID):
    member = Member.objects.filter(id=ID).first()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aiv_{}_{}_{}.csv"'.format(SEM, SY, member)
    writer = csv.writer(response)
    writer.writerow(["Faculty Member",member])
    writer.writerow(["Criterion", "First Visit", "Second Visit", "Average", "Remarks"])
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
    aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating)
    for item in aivcriterionscores:
        writer.writerow([item.aivcriterion,item.first_visit,item.second_visit,item.average_score,item.remarks])
    return response 

#PDF
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
        aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating).all()

        value = settings.BASE_DIR
        temp = os.path.join(value, "aiv", "templates", "aiv", "temp.html")
        open(temp, "w+").write(render_to_string('aiv/updateaivevalscores_temp.html', 
        {"aivcriterionscores": aivcriterionscores, "member": member, "SY": SY, "SEM": SEM}))
         
        # getting the template
        pdf = html_to_pdf('aiv/temp.html')
         
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')