# # interactuar con el ORM:
# from django.db import models

# class User(models.Model):

#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     first_name= models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     id_admin = models.BooleanField(default=False)

#     # Incluye mas texto que un charfield
#     bio = models.TextField(blank=True)

#     birthdate = models.DateField(blank=True, null=True)
    
#     # Cuando se cree la instancia en la BD automaticamente le agrega la fecha:
#     created = models.DateTimeField(auto_now_add=True)
#     # Guarda la fecha en la que se edito por ultima vez:
#     modify = models.DateTimeField(auto_now=True)
    
#     # Para que por default regrese cierto dato como representativo...
#     def __str__(self):
#         return self.email