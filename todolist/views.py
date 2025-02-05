from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import List
import uuid
import datetime

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

    return render(request, "form.html", context)

def submit_form(request):
    new_list = List(
        text=request.POST["note"],
        # due_date=datetime.datetime.strptime(request.POST['due_date'], '%Y-%m-%d').date(),
        due_date=request.POST["due_date"],
    )
    new_list.save()

    return redirect('/list')
    # data = {
    #     'id': uuid.uuid4,
    #     'text': request.POST['note'],
    #     'due_date': datetime.strptime(request.POST['due_date'], '%m/%d/%y %H:%M:%S'),
    #     'is_done': False,
    # }


