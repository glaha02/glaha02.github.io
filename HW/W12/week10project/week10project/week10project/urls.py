from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu410125015', views.ccu410125015_function)
]
