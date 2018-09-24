from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.reference_list, name='reference_list'),
	path('<str:slug>/', views.reference_detail, name='reference_detail'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]