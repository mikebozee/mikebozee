from django.shortcuts import render, get_object_or_404

from .models import Profile


def profile_list(request):
	profiles = Profile.objects.order_by('last_name')
	return render(request, 'profiles/list.html', {'profiles': profiles})


def profile_detail(request, slug):
	profile = get_object_or_404(Profile, slug=slug)
	return render(request, 'profiles/detail.html', {'profile': profile})
