# Generated by Django 2.0.7 on 2018-08-13 05:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20180812_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
