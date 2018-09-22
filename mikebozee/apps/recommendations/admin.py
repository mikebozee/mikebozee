from django.contrib import admin

from .models import Recommendation


class RecommendationAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("first_name", "last_name",)}


admin.site.register(Recommendation, RecommendationAdmin)