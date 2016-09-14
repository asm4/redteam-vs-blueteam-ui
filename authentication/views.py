from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/team')  # TODO point to team page
            else:
                form.add_error(None, 'Could not find matching '
                               'username/password combination.')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
