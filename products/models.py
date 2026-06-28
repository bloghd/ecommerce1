from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class MainModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    
class Product(MainModel):
    name = models.CharField(_("Name"), max_length=100, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField(db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        related_name="products_category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
    )
    brand = models.ForeignKey(
        "Brand",
        related_name="products_brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
    )
    stock_quantity = models.PositiveIntegerField(db_index=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def Quantity(self):
        if self.stock_quantity == 0:
            return "Out of stock"
        else:
            return "In stock"
    
    def apply_discount(self, discount_percentage):
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = (discount_percentage / 100) * self.price
        discounted_price = self.price - discount_amount
        self.price = round(discounted_price, 2)
        return self.price
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = "products"


class Category(MainModel):
    name = models.CharField(_("Name"), max_length=100, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField(db_index=True)
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
        db_table = "categories"

class Brand(MainModel):
    name = models.CharField(_("Name"), max_length=100, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, blank=True)
    description = models.TextField(db_index=True)
    image = models.ImageField(upload_to="brands/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        db_table = "brands"


class ProductImage(MainModel):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
