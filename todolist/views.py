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
    return render(request, "form.html")

def list_form_update(request, rec_id):
    data = get_object_or_404(List, pk=rec_id)
    context = {
        "id": data.id,
        "text": data.text,
        "due_date": data.due_date
    }

    return render(request, "form.html", context)

def submit_form(request):
    data = {
        'id': request.POST['id'],
        'text': request.POST["note"],
        'due_date': request.POST["due_date"],
    }
    if request.POST['id']:
        rec = get_object_or_404(List, pk=int(data["id"]))
        rec.text = data["text"]
        rec.due_date = data["due_date"]
        rec.save()
    else:
        new_list = List(
            text=data.text,
            due_date=data.due_date,
        )
        new_list.save()

    return redirect('/list')

def delete_list(request, rec_id):
    data = get_object_or_404(List, pk=rec_id)
    data.delete()
    return redirect('/list')

def record_is_done(request, rec_id):
    data = get_object_or_404(List, pk=rec_id)
    data.is_done = not data.is_done
    data.save()
    return redirect('/list')
