from django.contrib import admin
from django.urls import path, include
from users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_view.register, name="register"),
    path('', include('blog.urls')),
]
