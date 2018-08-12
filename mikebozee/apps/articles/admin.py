from django import forms
from django.contrib import admin

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article


class ArticleAdminForm(forms.ModelForm):
	text = RichTextUploadingField()
	image = RichTextUploadingField()
	class Meta:
		model = Article
		fields = ['author', 'title', 'text', 'created_date', 'published_date', 'slug', 'image', 'tags']


class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)