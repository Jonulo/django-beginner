# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    # Todo lo que queremos que se vea en detalles:
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # Para que los siguientes datos sean LINKS que nos lleven a los detalles:
    list_display_links = ('pk', 'user')
    # hacemos que se pueda editar desde el preview sin entrar a detalles:
    list_editable = ('phone_number', 'website', 'picture')
    # Agregar campo se búsqueda y los parámetros por los que buscara
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # Agregar tabla de filtros a la derecha para filtrar por creación o modificación
    list_filter = ('created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )
    # ****
    # Fieldsets es un tupla que con tiene más tuplas con la configuración de DETALLES
    fieldsets = (
        # Esta es una tupla con dos elementos, el título de la categoria y un diccionario
        ('Profile', {
            # aqui se crean la tuplas de como se va a visualizar horizontal o vertical
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )
    # Todos los campos aqui NO SE PUEDEN EDITAR cuando accedas el detalle de ellos
    readonly_fields = ('created', 'modified', 'user')

# Ahora, para tener dos modelos en uno y no navegar entre varios para registrar
# datos relacionados:

class ProfileInline(admin.StackedInline):
    # De que modelo es el stackedInline
    model = Profile

    can_delete = False
    verbose_name_plural = 'profiles'

# Hereda del base y le agregamos el inline que es nuestro modelo
class UserAdmin(BaseUserAdmin):
    
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# Quitamos el modelo base USER y agregamos el nuestro con los dos modelos "CONCATENADOS"
admin.site.unregister(User)
admin.site.register(User, UserAdmin)