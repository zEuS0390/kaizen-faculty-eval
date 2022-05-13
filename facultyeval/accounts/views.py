from email.message import EmailMessage
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from .forms import UserForm, PassResetForm
from .decorators import unauthenticated_user
from .models import Member
from django.core.mail import mail_admins

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
                return redirect("member:home")
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
            mail_admins("New Registrant","A new member has successfully registered.")           
            return redirect("accounts:login")
        errors = [' '.join(error for error in errorlist) for errorlist in form.errors.values()]
        for error in errors:
            messages.error(request, f"{error}")
        return render(request, template_name="accounts/register.html", context={"form": form})

class PassResetView(PasswordResetView):
    form_class = PassResetForm

@login_required(login_url="/accounts/login/")
def logoutUser(request):
    """
    This view will log out the authenticated user.
    """
    logout(request)
    return redirect("/")