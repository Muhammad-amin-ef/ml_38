from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    image = models.ImageField(_('image'), upload_to='products/', blank=True, null=True)
    brand = models.CharField(_('brand'), max_length=100, blank=True, null=True)
    details = models.TextField(_('details'), blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(_('quantity'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')