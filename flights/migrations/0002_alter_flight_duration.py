# Generated by Django 3.2.8 on 2021-11-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(),
        ),
    ]