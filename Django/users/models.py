from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


# Create your models here.

class User(AbstractUser):
    def get_full_name(self) -> str:
        def get_full_name(self):
            return '{}, {}'.format(self.first_name, self.last_name)



class Cliente(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    biografia =models.TextField()
