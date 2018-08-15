from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.position_list, name='position_list'),
	path('<str:slug>/', views.position_detail, name='position_detail'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]