from django.shortcuts import redirect

def member_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect("administrator:dashboard")
        return view_func(request, *args, **kwargs)
    return wrapper_func