import uuid
import decimal
from django.db import models
from DirEnvio.models import DireccionEnvio
from users.models import User
from cart.models import Cart
from django.db.models.signals import pre_save
from .comun import OrdenStatus,choices
from .comun import choices
from promo_codigo.models import PromoCodigo


# Create your models here.

class Orden(models.Model):
    ordenID = models.CharField(max_length=100,null=False, unique=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=choices, default=OrdenStatus.CREATED )
    envio_total = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.ForeignKey(DireccionEnvio, null=True , blank=False, on_delete=models.CASCADE)
    promo_codigo = models.OneToOneField(PromoCodigo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.ordenID
    
    def aplicarCodigo(self, promo_codigo):
        if self.promo_codigo is None:
            self.promo_codigo = promo_codigo
            self.save()

            self.update_total()
            promo_codigo.codigo_usado()
            
    
    def get_descuento(self):
        if self.promo_codigo:
            return self.promo_codigo.descuento
        
        return 0
    
    def get_total(self):
        return self.cart.total + self.envio_total - decimal.Decimal(self.get_descuento())
    
    def update_total(self):
        self.total = self.get_total()
        self.save()

    def get_or_set_DireccionEnvio(self):
        if self.direccion_envio:
            return self.direccion_envio
        
        direccion_envio=self.user.direccion_envio
        if direccion_envio:
            self.update_direction_envio = (direccion_envio)
            
        return direccion_envio
    
    def cancelar(self):
        self.status = OrdenStatus.CANCELED
        self.save()

    def completado(self):
        self.status = OrdenStatus.COMPLETED
        self.save()
    
    def update_direction_envio(self, direccion_envio):
        self.direccion_envio = direccion_envio
        self.save()
    
def enviarOrden(sender, instance, *args, **kwargs):
    if not instance.ordenID:
        instance.ordenID = str(uuid.uuid4())

def enviar_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()
        

pre_save.connect(enviarOrden, sender=Orden)
pre_save.connect(enviar_total, sender=Orden)