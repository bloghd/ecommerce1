from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Brand, Category, Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class CategoryListView(ListView):
    model = Category
    template_name = "products/category_list.html"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "products/category_detail.html"

class BrandListView(ListView):
    model = Brand
    template_name = "products/brand_list.html"

class BrandDetailView(DetailView):
    model = Brand
    template_name = "products/brand_detail.html"