# berechnung_benutzungsstunden\urls.py Datei
from django.urls import path
from django.contrib import admin
from . import tasks

urlpatterns = [
    path('admin/upload/', admin.site.admin_view(tasks.upload_excel), name='admin_upload'),
    #path('upload/', tasks.upload_excel, name='upload'),
    path('results/', tasks.results, name='results'),
    path('clean-results/', tasks.cleaned_data, name='cleaned_data'),
    ]