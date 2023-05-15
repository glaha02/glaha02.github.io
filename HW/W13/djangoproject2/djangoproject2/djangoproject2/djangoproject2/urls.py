from djangoproject2 import views
from django.urls import path

from django.contrib import admin
urlpatterns = [
    path("", views.home),
    path("ccu410125015", views.ccu410125015_function),
    path("admin/", admin.site.urls)
]
