# Generated by Django 2.0.7 on 2018-09-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
