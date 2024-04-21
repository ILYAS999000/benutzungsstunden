# tasks.py in Ihrer Django-App
import pandas as pd
import numpy as np
import os
from django.shortcuts import render, redirect
from .forms import UploadExcelForm
from .models import EnergyUsage
from collections import defaultdict
from django.contrib.auth.decorators import login_required


# Funktion zum Aufteilen der Excel-Datei in separate Dateien
def split_excel_file(excel_file):
    excel_data = pd.ExcelFile(excel_file)
    sheet_names = excel_data.sheet_names

    # Erstellen eines Verzeichnisses zum Speichern der getrennten Dateien
    output_dir = 'output/'
    os.makedirs(output_dir, exist_ok=True)

    # Iterieren durch die Blätter und speichern jedes Blatt in einer separaten Excel-Datei
    for sheet_name in sheet_names:
        df = excel_data.parse(sheet_name)

        # Dateipfad für die separate Excel-Datei erstellen
        output_file_path = os.path.join(output_dir, f'{sheet_name}.xlsx')

        # DataFrames direkt in separate Excel-Dateien schreiben
        df.to_excel(output_file_path, index=False)


pass


# Ihre Upload-Funktion mit Berechnungen und Verarbeitung der separaten Dateien
@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']

            # Aufteilen der Excel-Datei in separate Dateien
            split_excel_file(excel_file)

            # Verarbeiten der separaten Excel-Dateien
            for root, _, files in os.walk('output/'):
                for file in files:
                    file_path = os.path.join(root, file)
                    excel_data = pd.read_excel(file_path)

                    # Berechnungen für dieses Blatt durchführen
                    (total_energy, highest_kw, second_highest_kw, usage_hours_highest_kw, usage_hours_second_highest_kw,
                     year_description) = calculate_usage(excel_data)

                    # Kundennummer aus Zelle B2 des DataFrames extrahieren
                    customer_number = excel_data.iloc[0, 1]  # Zeile 2 (Index 0), Spalte 2 (Index 1)

                    # Jahr aus Zelle B13 des DataFrames extrahieren
                    year = excel_data.iloc[11, 1]  # Zeile 13 (Index 11), Spalte 2 (Index 1)

                    # Ergebnisse in die Datenbanktabelle EnergyUsage eintragen
                    EnergyUsage.objects.create(
                        customer_number=customer_number,
                        year=year,
                        highest_kw=highest_kw,
                        second_highest_kw=second_highest_kw,
                        usage_hours_highest_kw=usage_hours_highest_kw,
                        usage_hours_second_highest_kw=usage_hours_second_highest_kw,
                        year_description=year_description
                    )

            # Bereinigen Sie die Daten
            cleaned_data(request)

            return redirect('results')
    else:
        form = UploadExcelForm()
    return render(request, 'berechnung_benutzungsstunden/upload.html', {'form': form})


def calculate_usage(excel_data):
    # Implementieren Sie die Logik für calculate_usage hier
    # Einlesen der Excel-Daten mit Pandas
    # df = pd.read_excel(excel_data)

    # Extrahieren der Werte aus der Spalte F (angenommen, die Daten beginnen in Zeile 3)
    # Sie können die Startzeile anpassen, falls Ihre Daten in einer anderen Zeile beginnen.
    values = excel_data.iloc[1:, 5].astype(float)  # Zeile 3, Spalte F

    # Überprüfen der Anzahl der Werte
    num_values = len(values)
    if num_values == 35040:
        year_description = "Es handelt sich um ein ganzes Jahr, also 365 Tage, kein Schaltjahr"
    elif num_values == 35136:
        year_description = "Es handelt sich um ein Schaltjahr, also 366 Tage"
    else:
        year_description = "Kein Jahr, entweder weniger als 365 Tage oder mehr als 366 Tage"

    # Berechnung der Gesamtenergie (total_energy) in kWh
    total_energy = values.sum() / 4

    # Sortieren der Werte in absteigender Reihenfolge, um den höchsten und zweithöchsten Wert zu finden
    sorted_values = np.sort(values)[::-1]

    # Höchster kW-Wert
    highest_kw = sorted_values[0]

    # Zweithöchster kW-Wert
    second_highest_kw = sorted_values[1] if len(
        sorted_values) > 1 else 0  # Wenn nur ein Wert vorhanden ist, ist der zweithöchste Wert 0

    # Berechnung der Benutzungsstunden
    usage_hours_highest_kw = total_energy / highest_kw
    usage_hours_second_highest_kw = total_energy / second_highest_kw if second_highest_kw > 0 else 0
    # Schutz vor Division durch null

    return (total_energy, highest_kw, second_highest_kw, usage_hours_highest_kw, usage_hours_second_highest_kw,
            year_description)


def results(request):
    # Implementieren Sie die Logik für results
    # hier können Sie die Ergebnisse aus der Datenbank abrufen und auf der Webseite anzeigen
    results = EnergyUsage.objects.all()
    return render(request, 'berechnung_benutzungsstunden/results.html', {'results': results})


def cleaned_data(request):
    # Holen Sie alle Datensätze aus der Datenbank
    all_energy_usage = EnergyUsage.objects.all()

    # Verwenden Sie ein default dict, um Datensätze mit demselben Kundennummer-Jahr-Paar zu speichern
    unique_records = defaultdict(list)

    # Iterieren Sie durch die Datensätze und fügen Sie sie in das default dict ein
    for record in all_energy_usage:
        key = (record.customer_number, record.year)
        unique_records[key].append(record)

    # Bereinigen Sie die Datenbank von Duplikaten
    for key, records in unique_records.items():
        # Wenn es mehr als einen Datensatz für dasselbe Kundennummer-Jahr-Paar gibt, behalten Sie nur einen
        if len(records) > 1:
            # Lassen Sie nur den ersten Datensatz in der Datenbank und löschen Sie die anderen
            records_to_keep = records[0]
            records_to_delete = records[1:]
            for record in records_to_delete:
                record.delete()

    # Hier können Sie die bereinigten Daten abrufen und auf der clean_results.html-Seite anzeigen
    cleaned_data = EnergyUsage.objects.all().order_by('customer_number')
    return render(request, 'berechnung_benutzungsstunden/clean_results.html', {'cleaned_data': cleaned_data})
