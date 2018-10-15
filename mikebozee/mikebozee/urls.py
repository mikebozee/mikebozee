"""mikebozee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_aepp import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('articles/', include('articles.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', include('apps.articles.urls')),
    path('educations/', include('apps.educations.urls')),
    path('positions/', include('apps.positions.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('projects/', include('apps.projects.urls')),
    path('references/', include('apps.references.urls')),
    path('stages/', include('apps.stages.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
