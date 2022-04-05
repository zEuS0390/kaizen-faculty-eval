from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Profile(View):

    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        return render(request, template_name="member/profile.html", context={})

    @method_decorator(login_required(login_url="accounts:login"))
    def post(self, request):
        return redirect("/member/")