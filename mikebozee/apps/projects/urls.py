from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.project_list, name='project_list'),
	path('<str:slug>/', views.project_detail, name='project_detail'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]