# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import torrentModel
from .forms import torrentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    allTorrents = torrentModel.objects.all()
    paginator = Paginator(allTorrents, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        torrents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        torrents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        torrents = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'torrents': torrents})



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

def torrent_details(request, pk):
    x = torrentModel.objects.get(pk=pk)
    context = {
        "obj": x,
    }
    return render (request,"details.html",context)
