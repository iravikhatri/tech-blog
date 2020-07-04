from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('work/', views.work, name="blog-work")
]
