from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .decorators import unauthenticated_user

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
                return HttpResponse("<a href='/logout/'>Viewer's Page</a>")
        return HttpResponse("<h1>Access Denied!</h1>")

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
            return redirect("accounts:login")
        return HttpResponse("<h1>Error!</h1>")

@login_required(login_url="/accounts/login/")
def logoutUser(request):
    """
    This view will log out the authenticated user.
    """
    logout(request)
    return redirect("/")

class Landing(View):

    @method_decorator(unauthenticated_user)
    def get(self, request):
        return render(request, template_name="accounts/landing.html", context={})

    @method_decorator(unauthenticated_user)
    def post(self, request):
        return redirect("/")