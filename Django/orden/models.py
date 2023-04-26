import uuid
from django.db import models
from users.models import User
from cart.models import Cart
from enum import Enum
from django.db.models.signals import pre_save

# Create your models here.

class OrdenStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

choices = [ (tag, tag.value) for tag in OrdenStatus]

class Orden(models.Model):
    ordenID = models.CharField(max_length=100,null=False, unique=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=choices, default=OrdenStatus.CREATED )
    envio_total = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ordenID
    
    def get_total(self):
        return self.cart.total + self.envio_total
    
    def update_total(self):
        self.total = self.get_total()
        self.save()
    
def enviarOrden(sender, instance, *args, **kwargs):
    if not instance.ordenID:
        instance.ordenID = str(uuid.uuid4())

def enviar_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()
        

pre_save.connect(enviarOrden, sender=Orden)
pre_save.connect(enviar_total, sender=Orden)