# Generated by Django 2.0.7 on 2018-09-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0005_remove_position_current'),
        ('recommendations', '0003_auto_20180922_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='positions',
            field=models.ManyToManyField(blank=True, null=True, to='positions.Position'),
        ),
    ]