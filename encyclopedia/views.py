from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util
from django.urls import reverse
from .forms import EntryForm, EditForm
import random
import markdown2

def index(request): 
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def listEntry(request):
    return render(request, 'encyclopedia/listEntry.html', {
    "entries": util.list_entries()
})    

def EntryPage(request, entryPage):
    if not util.get_entry(entryPage):
        return render(request, 'encyclopedia/entryError.html')
    return render(request, 'encyclopedia/entryPage.html', {
        "entryPage": markdown2.markdown(f'{util.get_entry(entryPage)}'),
        'entryName': entryPage
    })
def SearchEntry(request):
    li = []
    entryName = request.GET['q']
    if util.get_entry(entryName):
        return render(request, 'encyclopedia/entryPage.html', {
        "entryPage": markdown2.markdown(f'{util.get_entry(entryName)}'),
        "entryName": entryName
    })
    else:    
        for i in util.list_entries():
            if entryName in i:
                li.append(i)
        if not li:
            return render(request, 'encyclopedia/entryError.html')
        return render(request, "encyclopedia/listEntry.html", {
        "entries": li
        })            
def AddEntry(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            util.save_entry(form.cleaned_data['name'], form.cleaned_data['content'])
            return render(request, 'encyclopedia/entryPage.html', {
        "entryPage": markdown2.markdown(f"{util.get_entry(form.cleaned_data['name'])}"),
        "entryName": form.cleaned_data['name']
        
    })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()  
        return render(request, 'encyclopedia/addentry.html', {
            'form': form
        })
def editEntry(request, entryName):
    if not util.get_entry(entryName):
        return render(request, 'encyclopedia/entryError.html')
    form = EditForm(initial={'name': entryName, 'content': util.get_entry(entryName)})
    return render(request, 'encyclopedia/editEntry.html', {
        "entryPage": markdown2.markdown(f'{util.get_entry(entryName)}'),
        'form': form
    })
def randomChoice(request):
    entry = markdown2.markdown(util.get_entry(random.choice(util.list_entries())))
    return render(request, 'encyclopedia/entryPage.html', {
        "entryPage": entry,
        'entryName': "entry.title"
    })