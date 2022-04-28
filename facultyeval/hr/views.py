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
from django.forms import inlineformset_factory

# Create your views here.
class Index(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        members = Member.objects.all()
        return render(request, template_name="hr/index.html", context={"members":members})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")

class CreateEval(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request, ID):
        context = {
            "form": HRCriterionScoresForm()
        }
        return render(request, template_name="hr/evaluation_form_entry.html", context=context)

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")