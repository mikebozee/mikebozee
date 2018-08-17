from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.education_list, name='education_list'),
	path('<str:slug>/', views.education_detail, name='education_detail'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]