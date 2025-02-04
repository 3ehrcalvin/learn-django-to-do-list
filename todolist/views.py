from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import List

# Create your views here.

def home(request):
    todolist = List.objects.all().values()
    template = loader.get_template('list.html')

    context = {
        'list': todolist
    }

    return HttpResponse(template.render(context))

def list_form(request):
    template = loader.get_template('form.html')

    context = {
        
    }

    return HttpResponse(template.render(context))
