from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import *


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'brand', 'price', 'quantity', 'category')