from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.stage_list, name='stage_list'),
	path('<str:slug>/', views.stage_detail, name='stage_detail'),
]