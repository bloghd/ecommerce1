from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Brand, Category, Product


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "inventory/product_detail.html"
