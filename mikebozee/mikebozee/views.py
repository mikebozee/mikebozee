from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from apps.articles.models import Article
from apps.educations.models import Education
from apps.positions.models import Position
from apps.profiles.models import Profile
from apps.projects.models import Project
from apps.references.models import Reference

def index(request, template='base.html'):
	context = {
		'articles':   	Article.objects.all(),
		'educations': 	Education.objects.all(),
		'positions':  	Position.objects.all(),
		'profiles':   	Profile.objects.all(),
		'projects':   	Project.objects.all(),
		'references':	Reference.objects.all(),
	}
	return render(request, template, context)