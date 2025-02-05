from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.home, name="list"),
    path("form/", views.list_form, name="form"),
    path("form/<int:rec_id>", views.list_form_update, name="form"),
    path("form/submit", views.submit_form, name="submit"),
    path("delete/<int:rec_id>", views.delete_list, name="delete"),
    path("done/<int:rec_id>", views.record_is_done, name="done"),
]
