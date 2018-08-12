from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.article_list, name='article_list'),
	path('<str:slug>/', views.article_detail, name='article_detail'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]