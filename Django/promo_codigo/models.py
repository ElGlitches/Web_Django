from django.db import models
from django.db.models.signals import pre_save
import string, random 

# Create your models here.

class PromoCodigo(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descuento = models.FloatField(default=0.0)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo
    
def set_codigo(sender, instance, *args, **kwargs):
    if instance.codigo:
        return
    
    coders = string.ascii_uppercase + string.digits
    instance.codigo = ''.join(random.choice(coders) for _ in range(5)) 

pre_save.connect(set_codigo, sender = PromoCodigo)
