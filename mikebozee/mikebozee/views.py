from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from apps.articles.models import Article
from apps.educations.models import Education
from apps.positions.models import Position
from apps.profiles.models import Profile
from apps.projects.models import Project
from apps.references.models import Reference
from apps.stages.models import Stage

def index(request, template='base.html'):
	context = {
		'articles':   	Article.objects.filter(published=True, published_date__lte=timezone.now()).order_by('published_date'),
		'educations': 	Education.objects.all(),
		'positions':  	Position.objects.all(),
		'profiles':   	Profile.objects.all(),
		'projects':   	Project.objects.filter(published=True),
		'references':	Reference.objects.filter(published=True),
		'stages':		Stage.objects.all(),
	}
	return render(request, template, context)