from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.home, name="list"),
    path("form/", views.list_form, name="form"),
    path("form/submit", views.submit_form, name="submit"),
]
