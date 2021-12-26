from django.urls import path

from registration import views

app_name = "registration"
urlpatterns = [
    path("entry/create/", views.EntryCreate.as_view(), name="entry_create"),
]
