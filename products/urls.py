from django.urls import path

from .views import (
    BrandDetailView,
    BrandListView,
    CategoryDetailView,
    CategoryListView,
    ProductDetailView,
    ProductListView,
)

app_name = "products"

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("brands/", BrandListView.as_view(), name="brand_list"),
    path("brands/<slug:slug>/", BrandDetailView.as_view(), name="brand_detail"),


]