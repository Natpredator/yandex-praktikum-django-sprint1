from django.contrib import admin
from django.urls import path, include

app_name = 'blogicum'  # Это должно быть здесь

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
]

