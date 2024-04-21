# forms.py Datei
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


def validate_file_size(value):
    limit = 10 * 1024 * 1024  # 10 MB
    if value.size > limit:
        raise ValidationError('Datei zu groß. Größe sollte nicht größer als 10 MB sein.')


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(
        label='Excel-Datei hochladen',
        help_text='Wählen Sie eine Excel-Datei aus',
        validators=[FileExtensionValidator(['xlsx']), validate_file_size],
        )
