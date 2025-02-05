from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, "form.html", context)

def submit_form(request):
    new_list = List(
        text=request.POST["note"],
        due_date=request.POST["due_date"],
    )
    new_list.save()

    return redirect('/list')

def delete_list(request, rec_id):
    data = get_object_or_404(List, pk=rec_id)
    data.delete()
    return redirect('/list')


