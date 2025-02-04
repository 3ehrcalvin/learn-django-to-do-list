from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.home, name="Home"),
    path("form/", views.list_form, name="Form"),
    path("form/submit", views.list_form, name="Form"),
]
