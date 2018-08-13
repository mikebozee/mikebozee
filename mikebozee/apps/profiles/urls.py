from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.profile_list, name='profile_list'),
	path('<str:slug>/', views.profile_detail, name='profile_detail'),
]