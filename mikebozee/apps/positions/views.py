from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Position
from apps.references.models import Reference


def position_list(request):
	positions = Position.objects.all()
	return render(request, 'positions/list.html', {'positions': positions})


def position_detail(request, slug, template='positions/detail.html'):
	context = {
		'position':		get_object_or_404(Position, slug=slug),
		'references':	Reference.objects.filter(published=True),
	}
	return render(request, template, context)
