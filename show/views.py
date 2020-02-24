from django.shortcuts import render
from .models import Html
from django.core.files import File


def home(request):
    graphs = Html.objects.all()
    return render(request, 'show/home.html', {'graphs':graphs})


def graph(request):
    id = request.GET.get('id')
    return render(request, str(id[15:]))