from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .decorators import unauthenticated_user
from .models import Member

# Create your views here.
class Login(View):
    """
    The log in view will be the main entry point of the application. It would 
    require user credentials to verify if they are registered within the database.
    """

    @method_decorator(unauthenticated_user)
    def get(self, request):
        return render(request, template_name="accounts/login.html")

    @method_decorator(unauthenticated_user)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("administrator:dashboard")
            else:
                return redirect("member:profile")
        messages.error(request, "Incorrect username or password.")
        return redirect("accounts:login")

class Register(View):
    """
    The register view will essentially create a user and it will require
    basic information to be verified in the authentication.
    """

    @method_decorator(unauthenticated_user)
    def get(self, request):
        form = UserForm()
        return render(request, template_name="accounts/register.html", context={"form":form})

    @method_decorator(unauthenticated_user)
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            middle_name = form.cleaned_data.get('middle_name')
            member = Member(user=user, middle_name=middle_name)
            member.save()
            return redirect("accounts:login")
        return render(request, template_name="accounts/register.html", context={"form": form})

@login_required(login_url="/accounts/login/")
def logoutUser(request):
    """
    This view will log out the authenticated user.
    """
    logout(request)
    return redirect("/")