from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Recommendation


def recommendation_list(request):
	recommendations = Recommendation.objects.all()
	return render(request, 'recommendations/list.html', {'recommendations': recommendations})


def recommendation_detail(request, slug):
	recommendation = get_object_or_404(Recommendation, slug=slug)
	return render(request, 'recommendations/detail.html', {'recommendation': recommendation})
