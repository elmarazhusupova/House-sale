from django.shortcuts import render, redirect

from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from account.forms import LoginForm, UserRegisterForm
from account.models import User


class LoginView(FormView):
    form_class = LoginForm
    template_name = "account/login.html"

    def form_valid(self, form):
        data = form.cleaned_data
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index")
            return HttpResponse("Ваш аккаунт не активен!")
        return HttpResponse("Введенные вами данные некорректные!")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password_confirm')

        if password == password2:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('index')
        else:
            return redirect('register')
    else:
        return render(request, 'account/register.html')

