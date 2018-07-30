from django.urls import path

from . import views

urlpatterns = [
	path('', views.article_list, name='article_list'),
	# path('articles/', views.article_list, name='article_list'),
	path('<str:slug>/', views.article_detail, name='article_detail'),
]