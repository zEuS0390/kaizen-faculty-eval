from django.http import HttpResponse

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return HttpResponse("<a href='/logout/'>You are in the viewer's page.</a>")
    return wrapper_func