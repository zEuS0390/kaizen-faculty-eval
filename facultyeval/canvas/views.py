from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import admin_only

# Create your views here.
class Index(View):

    def get(self, request):
        return render(request, template_name="canvas/index.html")

class Canvas(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def get(self, request):
        return render(request, template_name="administrator/canvas.html", context={})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(admin_only)
    def post(self, request):
        return redirect("/")