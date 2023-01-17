from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was successfully created!')
            return redirect('login')

    context = {'form':form}
    return render(request, 'account/register.html', context)



def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)
