from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Project


def project_list(request):
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'projects/list.html', {'projects': projects})


def project_detail(request, slug):
	project = get_object_or_404(Project, slug=slug)
	return render(request, 'projects/detail.html', {'project': project})
