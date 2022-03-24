from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .decorators import check_user_auth

# Create your views here.
class Login(View):

    @method_decorator(check_user_auth)
    def get(self, request):
        return render(request, template_name="accounts\\login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("administrator:dashboard")
        return HttpResponse("<h1>Access Denied!</h1>")

class Register(View):

    def get(self, request):
        form = UserForm()
        return render(request, template_name="accounts\\register.html", context={"form":form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/accounts/login/")
        return HttpResponse("<h1>Error!</h1>")

@login_required(login_url="/accounts/login/")
def logoutUser(request):
    logout(request)
    return redirect("/")