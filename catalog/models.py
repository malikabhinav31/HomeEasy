from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7,decimal_places=2,validators = [MinValueValidator(0)])
    discount = models.DecimalField(max_digits=4,decimal_places=2,
                validators = [MinValueValidator(0),MaxValueValidator(100)])
    rating = models.DecimalField(max_digits=3,default=3,decimal_places=2,
                validators=[MinValueValidator(0),MaxValueValidator(5)])
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=500)
    brand_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class Variations(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
