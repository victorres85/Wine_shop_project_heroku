from atexit import register
from django.contrib import admin

from .models import Category, Country, Region, Wine

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country', 'slug', 'new_old_world']
    prepopulated_fields = {'slug': ('country',)}


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region', 'slug', 'country']
    prepopulated_fields = {'slug': ('region',)}


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ['wine_name', 'slug', 'vintage',
                    'wine_producer', 'country',
                    'region', 'category', 'description',
                    'price', 'cost', 'available', 'created_by']
    prepopulated_fields = {'slug': ('wine_name',)}
    list_filter = ['available', 'country', 'region',
                   'wine_name', 'vintage', 'price', 'cost']
    list_editable = ['available', 'vintage', 'price', 'cost']
