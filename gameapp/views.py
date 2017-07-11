from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.conf import settings
from django.utils import timezone

from . import forms, models

def index(request):
    if timezone.now() < settings.EVENT_START:
        return render(request, 'prehack.html', context={'time_left': settings.EVENT_START-timezone.now(),
            'start_time': settings.EVENT_START})
    if timezone.now() >  settings.EVENT_START + settings.EVENT_DURATION:
        return render(request, 'posthack.html')
    if not request.user.is_authenticated():
        return render(request, 'home.html')

    level = request.user.level
    if level >= len(settings.LEVEL_INFO):
        return render(request, 'congrats.html')

    wrong_solution = False
    level_filename, level_answer = settings.LEVEL_INFO[level]
    if request.method == 'POST':
        form = forms.SolutionForm(request.POST)
        if form.is_valid():
            solution = form.cleaned_data['solution'].lower()
            if solution in level_answer:
                request.user.level += 1
                request.user.level_date = timezone.now()
                request.user.save()
                return HttpResponseRedirect("/")
            else:
                wrong_solution = True
    else:
        form = forms.SolutionForm()

    return render(request, 'level.html', {
        'form': form.as_p(),
        'level': level,
        'template': 'levels/{}'.format(level_filename),
        'wrong_solution': wrong_solution
    })

def ranking(request):
    users = models.User.objects.filter(level__gt=0).order_by('-level', 'level_date')
    contest_running = timezone.now() > settings.EVENT_START and timezone.now() < settings.EVENT_START + settings.EVENT_DURATION
    return render(request, 'ranking.html', {
        'users': users,
        'contest_running': contest_running,
        'time_left': (settings.EVENT_START + settings.EVENT_DURATION) - timezone.now(),
        'levellength': len(settings.LEVEL_INFO)})


def faq(request):
    return render(request, 'faq.html', context={
        'time_left': settings.EVENT_START-timezone.now(),
        'start_time': settings.EVENT_START,
        'end_time': settings.EVENT_START + settings.EVENT_DURATION,
        'num_problems': len(settings.LEVEL_INFO)
        })




def login(request):
    # if this is a POST request we need to process the form data
    bad_login = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                bad_login = True
    else:
        form = forms.LoginForm()

    return render(request, 'login.html', {'form': form.as_p(), 'bad_login': bad_login})

def register(request):
    # if this is a POST request we need to process the form data
    bad_username = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if models.User.objects.filter(username=username).first() is not None:
                bad_username = True
            else:
                user = models.User.objects.create_user(username=username, password=password)
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = forms.LoginForm()

    return render(request, 'register.html', {'form': form.as_p(), 'bad_username': bad_username})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return HttpResponseRedirect("/")
