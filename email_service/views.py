from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import SubscribedUsers
from .forms import SubscribedUsersForm
from mailing_service import settings
from celery import shared_task
from time import sleep


@shared_task
def index_view(request):
    if request.method == 'POST':
        for user in SubscribedUsers.objects.all():
            subject = request.POST['in_subject']
            message = request.POST['in_text']+'\n Уважаемый '+str(user.username)+' '+str(user.birth_date)
            duration = request.POST['in_duration']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = (user.email,)
            sleep(duration)
            send_mail(
                subject=subject,
                message=message,
                from_email=email_from,
                recipient_list=recipient_list
            )
            response = HttpResponse('Thanks. The mailing of messages has been completed')
            return response
    return render(request, 'index.html')


def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribedUsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            birth_date = form.cleaned_data['birth_date']
            SubscribedUsers.objects.create(
                username=user,
                email=email,
                birth_date=birth_date
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/index')
    else:
        form = SubscribedUsersForm()
    return render(request, 'subscribe.html', {'form': form})
