from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import member_only

# Create your views here.
class Profile(View):

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(member_only)
    def get(self, request):
        return render(request, template_name="member/profile.html", context={})

    @method_decorator(login_required(login_url="accounts:login"))
    @method_decorator(member_only)
    def post(self, request):
        return redirect("/member/")