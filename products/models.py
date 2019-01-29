from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, \
                                                null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title


    def  get_price (self):
        return self.price


    def get_absolute_url(self):
        return reverse('single_product', kwargs={'slug': self.slug})


class ProductImage(models.Model):
        product = models.ForeignKey(Product, on_delete=models.PROTECT)
        image = models.ImageField(default='default.png', blank=True)
        featured = models.BooleanField(default=False)
        thumbnail = models.BooleanField(default=False)
        active = models.BooleanField(default=True)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)

        def __str__(self):
            return self.product.title

