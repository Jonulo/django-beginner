from django.contrib import admin
from django.urls import path
# Importaciones para ver las imagenes cuando desarrollamos
from django.conf.urls.static import static
from django.conf import settings

#apps
from jonugram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('numbers/', local_views.get_numbers, name='numbers'),
    path('test/<str:name>/<int:age>/', local_views.test),

    # apps
    path('', posts_views.list_posts, name='feed'),
    path('posts/new', posts_views.create_post, name='create_post'),
    # Login
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile', users_views.update_profile, name='update_profile'),

# Le suma a urlpatterns una url estática con valor de MEDIA_URL y el path que estamos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
