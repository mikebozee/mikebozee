from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Education


def education_list(request):
	educations = Education.objects.all()
	return render(request, 'educations/list.html', {'educations': educations})


def education_detail(request, slug):
	education = get_object_or_404(Education, slug=slug)
	return render(request, 'educations/detail.html', {'education': education})
