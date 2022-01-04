import re
from django.forms.widgets import Textarea
from django.shortcuts import render
from . import util
from django import forms, urls
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound

from markdown2 import Markdown
from . import forms
from django.template import loader
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_convert(request, title):
    if util.get_entry!=None:
        page=util.get_entry(title)
        page_mark=Markdown().convert(page)
        return render(request, "encyclopedia/pages.html", {
            'page': page_mark,
            'title': title
        })



def search (request, title=None):
    articles=util.list_entries()
    if request.method=="GET":
        query = request.GET.get('q')
        for art in articles:
            if query.casefold() == art.casefold():
                get_convert(request, title)
        entries=[]
        for art in util.list_entries():
            if art.lower().find(query.lower()) !=-1:
                entries.append(art)
        return render(request, "encyclopedia/search.html", {
            'query': query,
            'entries': entries
            })
    return render(request, "encyclopedia/search.html", {
            'query': '',
            'entries': []
            })


def add_entry(request):
    if request.method == "POST":
        form=forms.NewEntryForm(request.POST)
        request.encoding = 'utf-8'
        if form.is_valid():
            title = request.POST["title"]
            content = request.POST["content"]
            util.save_entry (title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
    else:
        form =  forms.NewEntryForm()
            
    return render(request, "encyclopedia/new_art.html", {
        "form": forms.NewEntryForm(),
    })


def edit(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
            "form": forms.NewEntryForm({'title':title,'content':content}),
            "name": title
                })


def saveEdit(request):
    if request.method == "POST":
        form=forms.NewEntryForm(request.POST)
        request.encoding = 'utf-8'
        if form.is_valid():
            title = request.POST["title"]
            content = request.POST["content"]
            util.save_entry (title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
    else:
        form =  forms.NewEntryForm()
            
    return render(request, "encyclopedia/edit.html", {
        "form": forms.NewEntryForm(),
    })


def random_page(request, title=None):
    title=random.choice(util.list_entries())
    page=util.get_entry(title)
    page_mark=Markdown().convert(page)
    return render(request, "encyclopedia/pages.html", {
            'title': title,
            'page': page_mark,
        })

        
 
    