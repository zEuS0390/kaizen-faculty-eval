from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(View):
    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        return render(request, template_name="administrator/index.html", context={})

class HR(View):

    def get(self, request):
        return render(request, template_name="administrator/hr.html", context={})

    def post(self, request):
        return 

class AIV(View):

    def get(self, request):
        return render(request, template_name="administrator/aiv.html", context={})

    def post(self, request):
        return redirect("/")

class Canvas(View):

    def get(self, request):
        return render(request, template_name="administrator/canvas.html", context={})

    def post(self, request):
        return redirect("/")