# Generated by Django 2.0.7 on 2018-10-16 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0008_position_projects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['-start_date']},
        ),
    ]
