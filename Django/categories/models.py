from django.db import models
from products.models import Product

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
