from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Entry
from .forms import EntryForm

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # redirect
#         return HttpResponseRedirect('myapp/calendar.html')
#     else:
#         return HttpResponseRedirect('/')


def calendar(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/calendar.html', {'entries': entries})


def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry': entry})


def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            Entry.objects.create(
                name=name,
                date=date,
                description=description
            ).save()
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
    return render(request, 'myapp/form.html', {'form': form})


def delete(request, pk):
    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')
