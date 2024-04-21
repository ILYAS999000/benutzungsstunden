# admin.py
from django.contrib import admin
from .models import EnergyUsage  # Stellen Sie sicher, dass Sie das Modell korrekt importieren
from . import tasks
from django.urls import path

class CustomAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload/', self.admin_site.admin_view(tasks.upload_excel), name='admin_upload'),
        ]
        return custom_urls + urls

admin.site.register(EnergyUsage)