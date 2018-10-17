from django import forms
from django.contrib import admin

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Education


class EducationAdminForm(forms.ModelForm):
	text = RichTextUploadingField()
	image = RichTextUploadingField()
	class Meta:
		model = Education
		fields = ['title', 'institution', 'location', 'date', 'text', 'priority', 'created_date', 'slug', 'image', 'tags']


class EducationAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", "institution",)}
	form = EducationAdminForm


admin.site.register(Education, EducationAdmin)