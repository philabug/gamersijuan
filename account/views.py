from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.conf import settings


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("blog:home")
        else:
            messages.info(request, 'Email or Password is incorrect.')
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "login.html")


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)