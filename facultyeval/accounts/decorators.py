from django.shortcuts import redirect 

def check_user_auth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("administrator:dashboard")
        return view_func(request, *args,**kwargs)
    return wrapper_func