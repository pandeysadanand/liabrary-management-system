from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = '/auth/login/'


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request):
    form = LoginForm()
    context = {"form": form}
    if request.POST:
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login successful")
            return redirect("books:booklist")

        else:
            print("Login error")
            return redirect("auth:login")
    return render(request, "user/login.html", context)
