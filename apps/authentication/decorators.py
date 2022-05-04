from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import template
from django.template import loader

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


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user
            group = None
            if user.groups.exists():
                group = user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return render(request,'authentication/page-403.html', {"user": user})
                
        return wrapper_func
    return decorator