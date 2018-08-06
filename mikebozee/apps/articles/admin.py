from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from .models import Article


class ArticleAdminForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Article
		fields = ['author', 'title', 'text', 'created_date', 'published_date', 'slug']


class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)