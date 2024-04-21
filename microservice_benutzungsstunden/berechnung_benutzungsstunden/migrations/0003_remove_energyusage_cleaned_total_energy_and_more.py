# Generated by Django 4.2.5 on 2023-10-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berechnung_benutzungsstunden', '0002_energyusage_cleaned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='energyusage_cleaned',
            name='total_energy',
        ),
        migrations.AlterField(
            model_name='energyusage_cleaned',
            name='customer_number',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='energyusage_cleaned',
            name='highest_kw',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='energyusage_cleaned',
            name='second_highest_kw',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='energyusage_cleaned',
            name='usage_hours_highest_kw',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='energyusage_cleaned',
            name='usage_hours_second_highest_kw',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='energyusage_cleaned',
            name='year',
            field=models.CharField(max_length=10),
        ),
    ]