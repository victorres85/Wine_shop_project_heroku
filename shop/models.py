from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator
import datetime
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:wine_list_by_category', args=[self.slug])


class Country(models.Model):

    class NewOldWorlChoice(models.TextChoices):
        NEW_WORLD = "New World", "New World"
        OLD_WORLD = "Old World", "Old World"

    country = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    new_old_world = models.CharField(max_length=10,
                                     choices=NewOldWorlChoice.choices)

    class Meta:
        ordering = ['country']
        indexes = [
            models.Index(fields=['country']),
        ]

    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return reverse('shop:wine_list_by_country', args=[self.slug])


class Region(models.Model):
    region = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.ForeignKey(Country,
                                related_name='regions',
                                on_delete=models.CASCADE)

    class Meta:
        ordering = ['country']
        indexes = [
            models.Index(fields=['country']),
        ]

    def __str__(self):
        return self.region

    def get_absolute_url(self):
        return reverse('shop:wine_list_by_region', args=[self.slug])


class Wine(models.Model):
    wine_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    vintage = models.PositiveIntegerField(
        validators=[MaxValueValidator(datetime.date.today().year)])
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    wine_producer = models.CharField(max_length=200)
    country = models.ForeignKey(Country,
                                related_name='wine',
                                on_delete=models.CASCADE)
    region = models.ForeignKey(Region,
                               related_name='wine',
                               on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 related_name='wine',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)

    class Meta:
        ordering = ['wine_name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['wine_name']),
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.wine_name

    def get_absolute_url(self):
        return reverse('shop:wine_detail', args=[self.id, self.slug])
