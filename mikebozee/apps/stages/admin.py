from django import forms
from django.contrib import admin

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget

from .models import Stage


class StageAdminForm(forms.ModelForm):
	text = RichTextUploadingField()
	class Meta:
		model = Stage
		fields = ['title', 'location', 'start_date', 'end_date', 'text', 'created_date', 'slug']


class StageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", "location",)}
	form = StageAdminForm


admin.site.register(Stage, StageAdmin)