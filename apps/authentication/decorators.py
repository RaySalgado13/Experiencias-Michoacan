from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        #logical business here
        user = request.user
        if user.is_authenticated:
            user_groups = user.groups.all()
            for user_group in user_groups:
                return redirect(f"/{user_group}")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func