# Generated by Django 3.2.8 on 2021-11-14 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_flight_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='origin',
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
    ]
