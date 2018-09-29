from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title', 'published')


admin.site.register(Project, ProjectAdmin)