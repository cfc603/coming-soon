from django.contrib import admin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

    date_hierarchy = "created"
    fields = ("email",)
    list_display = ("created", "email")
    ordering = ("-created", "email")
