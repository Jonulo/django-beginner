from django.contrib import admin
from django.urls import path, include
# Importaciones para ver las imagenes cuando desarrollamos
from django.conf.urls.static import static
from django.conf import settings

#apps
from jonugram import views as local_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ejemplos nada que ve con la app
    path('numbers/', local_views.get_numbers, name='numbers'),
    path('test/<str:name>/<int:age>/', local_views.test),

    # Las url las agrupamos por aplicación, el primer parametro se le concatena
    # a cada url de la app.
    # apps
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    # Login
    path('users/', include(('users.urls', 'users'), namespace='users'))

# Le suma a urlpatterns una url estática con valor de MEDIA_URL y el path que estamos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
