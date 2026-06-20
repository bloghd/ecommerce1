from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        related_name="products_category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        "Brand",
        related_name="products_brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    stock_quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="brands/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
