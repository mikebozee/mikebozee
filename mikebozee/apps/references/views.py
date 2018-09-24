from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Reference


def reference_list(request):
	references = Reference.objects.all()
	return render(request, 'references/list.html', {'references': references})


def reference_detail(request, slug):
	reference = get_object_or_404(Reference, slug=slug)
	return render(request, 'references/detail.html', {'reference': reference})
