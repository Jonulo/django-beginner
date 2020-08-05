# interactuar con el ORM:
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # cuando se borre el usuario se borren los posts
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Hacer una importación circular, en lugar de importar arriba se hace así:
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title =models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @ {}'.format(self.title, self.user.username)