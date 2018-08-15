from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Position


def position_list(request):
	positions = Position.objects.all()
	return render(request, 'positions/list.html', {'positions': positions})


def position_detail(request, slug):
	position = get_object_or_404(Position, slug=slug)
	return render(request, 'positions/detail.html', {'position': position})
