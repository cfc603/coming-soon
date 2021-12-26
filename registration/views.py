from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Entry


class EntryCreate(CreateView):

    fields = ["email"]
    model = Entry
    success_url = reverse_lazy("home:landing")

    def form_invalid(self, form):
        return redirect(f"{self.get_success_url()}?error=true")

    def form_valid(self, form):
        self.object = form.save()
        return redirect(f"{self.get_success_url()}?success=true")

    def get_success_url(self):
        return self.success_url
