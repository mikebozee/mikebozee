from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('', views.recommendation_list, name='recommendation_list'),
	path('<str:slug>/', views.recommendation_detail, name='recommendation_detail'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]