from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def index(request):
	# return HttpResponse("Testing 123.")
	return render(request, '..templates/base.html', {})