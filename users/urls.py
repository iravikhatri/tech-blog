from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="users-login"),
    path('logout/', views.logout_view, name="users-logout"),
]
