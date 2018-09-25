from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Stage


def stage_list(request):
	stages = Stage.objects.all()
	return render(request, 'stages/list.html', {'stages': stages})


def stage_detail(request, slug):
	stage = get_object_or_404(Stage, slug=slug)
	return render(request, 'stages/detail.html', {'stage': stage})
