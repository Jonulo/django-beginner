from django.contrib import admin
from django.urls import path

#apps
from jonugram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('numbers/', local_views.get_numbers),
    path('test/<str:name>/<int:age>/', local_views.test),

    # apps
    path('posts/', posts_views.list_posts),
]
