from django.contrib import admin
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', users_views.login_view, name="users-login"),
    path('logout/', users_views.logout_view, name="users-logout"),
]
