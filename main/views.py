from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def index(request):
    banner = Banner.objects.all()
    about = AboutApartment.objects.all()
    feedback = ClientFeedback.objects.all()
    banner2 = Deal.objects.all()
    posts = HouseSale.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['number'],
                         form.cleaned_data['message'])
            return redirect('/')

    else:
        form = ContactForm()

    content = {'banner': banner, 'about': about, 'feedback': feedback,
               'form': form, 'banner2': banner2, 'posts': posts}
    return render(request, 'index.html', content)


def about(request):
    about = AboutApartment.objects.all()
    content = {'about': about}
    return render(request, 'about.html', content)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['number'],
                         form.cleaned_data['message'])
            return redirect('/')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)


def send_message(name, email, number, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'number': number, 'message': message}
    subject = 'Сообщениеот пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def feedbacck(request):
    name = ClientFeedback.objects.all()
    content = {'name': name}
    return render(request, content)


def deal(request):
    banner2 = Deal.objects.all()
    content = {'banner2': banner2}
    return render(request, content)


def price(request):
    return render(request, 'price.html')


def house(request):
    return render(request, 'house.html')


# def houseSale(request):
#     banner3 = HouseSale.objects.all()
#     content = {'banner3': banner3}
#     return render(request, content)
