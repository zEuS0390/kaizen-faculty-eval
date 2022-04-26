from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .decorators import admin_only
from django.views import View

# Create your views here.
class Index(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        return render(request, template_name="hr/index.html")

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")