from datetime import date
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm


def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/new_home.html', {'news': news})


def create(request):
    error = ''

    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.instance.date = date.today()
            form.save()
            return redirect('home')
        else:
            error = 'Form submission error. Please check your input.'

    else:
        form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


