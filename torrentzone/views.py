# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import torrentModel
from .forms import torrentForm
from django.shortcuts import redirect
# Create your views here.

def home(request):
    context = {
        "allTorrents": torrentModel.objects.all(),
    }
    return render(request,"home.html",context) #stwórz template home.html

def create(request):
    torrForm = torrentForm(request.POST or None)
    context = {
        "torForm": torrForm,
    }
    if torrForm.is_valid():
        instance = torrForm.save(commit=False)
        instance.torrentName = torrForm.cleaned_data.get('torrentName')
        instance.torrentLink = torrForm.cleaned_data.get('torrentLink')
        instance.save()
        return redirect("home")
    return render(request, "create.html", context)

def delete_torrent(request, pk):
    if request.user.is_authenticated():
        x = torrentModel.objects.get(pk=pk)
        x.delete()
        return redirect("home")
    return redirect("home")
