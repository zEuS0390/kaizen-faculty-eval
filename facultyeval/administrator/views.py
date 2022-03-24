from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(View):
    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        return render(request, template_name="administrator\index.html", context={})