from django import forms
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Position


class PositionAdminForm(forms.ModelForm):
	text = RichTextUploadingField()
	image = RichTextUploadingField()
	class Meta:
		model = Position
		fields = ['title', 'company', 'location', 'start_date', 'end_date', 'text', 'created_date', 'slug', 'image', 'logo', 'references', 'tags']


class PositionAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", "company",)}
	form = PositionAdminForm
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Position, PositionAdmin)