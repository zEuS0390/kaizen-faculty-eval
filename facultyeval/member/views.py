from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import member_only
from administrator.models import ActivityLogs
from accounts.models import Member
from hr.models import *
from aiv.models import *
from django.http import HttpResponse
import csv
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import View
from django.template.loader import render_to_string
from canvas.models import *
from .forms import *
from django.conf import settings
import os

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

class EditProfile(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(member_only)
    def get(self, request):
        member = Member.objects.filter(user=request.user).first()
        member_form = EditMemberForm(instance=member)
        user_form = EditUserForm(instance=request.user)
        context = {
            "member_form": member_form,
            "user_form": user_form
        }
        return render(request, template_name="member/edit_profile.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(member_only)
    def post(self, request):
        member = Member.objects.filter(user=request.user).first()
        member_form = EditMemberForm(request.POST, request.FILES, instance=member)
        user_form = EditUserForm(request.POST, instance=request.user)
        if member_form.is_valid() and user_form.is_valid():
            member_form.save()
            user_form.save()
        return redirect("member:profile")

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
def RedirectLMS(request):
    SEM = "1st-Sem"
    SY = "2021-2022"
    return redirect("member:lms", SEM=SEM, SY=SY)

@login_required(login_url="accounts:login")
@member_only
def LMS(request, SEM, SY):
    member = Member.objects.filter(user=request.user).first()
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    sy_group = SchoolYear.objects.all()
    mgratings = MGRating.objects.filter(member=member, semester=SEM, school_year=school_year).all()
    context = {
        "mgratings": mgratings,
        "SY": SY,
        "SEM": SEM,
        "sy_group": sy_group
    }
    return render(request, template_name="member/lms.html", context=context)

@login_required(login_url="accounts:login")
@member_only
def About(request):
    return render(request, template_name="member/about.html", context={})

#CSV HR
@login_required(login_url="accounts:login")
@member_only
def export_hr_csv(request,SEM, SY):
    member = Member.objects.filter(user=request.user).first()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hr_{}_{}_{}.csv"'.format(SEM, SY, member)
    writer = csv.writer(response)
    writer.writerow(["Faculty Member",member])
    writer.writerow(["Criterion", "Program Chair", "Student", "Average", "Remarks"])
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
    hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating).all()
    for item in hrcriterionscores:
        writer.writerow([item.hrcriterion,item.program_chair_score,item.student_score,item.average_score,item.remarks])
    return response 

#CSV AIV
@login_required(login_url="accounts:login")
@member_only
def export_aiv_csv(request,SEM, SY):
    member = Member.objects.filter(user=request.user).first()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aiv_{}_{}_{}.csv"'.format(SEM, SY, member)
    writer = csv.writer(response)
    writer.writerow(["Faculty Member",member])
    writer.writerow(["Criterion", "First Visit", "Second Visit", "Average", "Remarks"])
    school_year = SchoolYear.objects.filter(school_year=SY).first()
    aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
    aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating).all()
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

#PDF HR
class GeneratePdfHR(View):
    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(member_only)
    def get(self, request, SEM, SY):

        member = Member.objects.filter(user=request.user).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        hrrating = HRRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        hrcriterionscores = HRCriterionScores.objects.filter(hrrating=hrrating).all()
        
        value = settings.BASE_DIR
        temp = os.path.join(value, "member", "templates", "member", "temp.html")
        open(temp, "w").write(render_to_string('member/hrevalscores_temp.html', 
        {"hrcriterionscores": hrcriterionscores, "member": member, "SY": SY, "SEM": SEM}))
         
        # getting the template
        pdf = html_to_pdf('member/temp.html')
         
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#PDF AIV
class GeneratePdfAIV(View):
    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(member_only)
    def get(self, request, SEM, SY):

        member = Member.objects.filter(user=request.user).first()
        school_year = SchoolYear.objects.filter(school_year=SY).first()
        aivrating = AIVRating.objects.filter(member=member, school_year=school_year, semester=SEM).first()
        aivcriterionscores = AIVCriterionScores.objects.filter(aivrating=aivrating).all()

        value = settings.BASE_DIR
        temp = os.path.join(value, "member", "templates", "member", "temp.html")
        open(temp, "w").write(render_to_string('member/aivevalscores_temp.html', 
        {"aivcriterionscores": aivcriterionscores, "member": member, "SY": SY, "SEM": SEM}))
         
        # getting the template
        pdf = html_to_pdf('member/temp.html')
         
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')