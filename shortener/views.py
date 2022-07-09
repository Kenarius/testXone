from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from django.shortcuts import redirect
import pyshorteners


def main_view(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        user_form = forms.RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/registration_complete.html',
                          {'new_user': new_user})
        else:
            return HttpResponse('bad credentials')
    else:
        user_form = forms.RegistrationForm(request.POST)
        return render(request, 'registration/register_user.html', {"form": user_form})


def short_view(request):
    if request.method == 'POST':
        short_form = forms.ShortForm(request.POST)
        if short_form.is_valid():
            new_url = short_form.save(commit=False)
            if request.user.is_authenticated:
                new_url.author = request.user
                new_url.shorturl = pyshorteners.Shortener().tinyurl.short(new_url.fullurl)
                new_url.save()
                return redirect('shortener:myshorts/')
            else:
                return HttpResponse(pyshorteners.Shortener().tinyurl.short(new_url.fullurl))
    else:
        short_form = forms.ShortForm()
    return render(request,
                  'new_short.html',
                  {'form': short_form})


def myshorts_view(request):
    return render(request, "myshorts.html")
