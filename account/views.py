# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
# from django.contrib import messages


# def registerPage(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was successfully created!')
#             return redirect('login')

#     context = {'form':form}
#     return render(request, 'account/register.html', context)



# def loginPage(request):
#     context = {}
#     return render(request, 'account/login.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(request, 'register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('index')
        else:
            messages.info(request, 'Password not Matching')
            return redirect('register')
    else:
        return render(request, 'account/register.html')

def loginView(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('register')
    else:
        return render(request, 'account/register.html') 
