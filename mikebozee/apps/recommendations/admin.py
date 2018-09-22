from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Recommendation


class RecommendationAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("first_name", "last_name",)}
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Recommendation, RecommendationAdmin)