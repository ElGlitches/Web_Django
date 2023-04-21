from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from.models import Product

# Create your views here.

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Productos'
        return context



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

