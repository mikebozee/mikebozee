# Generated by Django 2.0.7 on 2018-09-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180813_2018'),
        ('recommendations', '0006_recommendation_educations'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='projects',
            field=models.ManyToManyField(blank=True, to='projects.Project'),
        ),
    ]