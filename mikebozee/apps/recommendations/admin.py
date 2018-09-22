from django.contrib import admin

from .models import Recommendation


class RecommendationAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Recommendation, RecommendationAdmin)