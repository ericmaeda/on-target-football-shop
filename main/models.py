import uuid
from django.db import models

# Create your models here.
class Product(models.Model) :

    ALL_CATEGORIES = [
        ('jersey', 'Jersey'),
        ('short', 'Short'),
        ('gloves', 'Gloves'),
        ('boots', 'Boots'),
        ('ball', 'Ball'),
        ('socks', 'Socks'),
        ('others', 'Others')
    ]

    ALL_BRANDS = [
        ('adios', 'Adios'),
        ('Niki', 'Niki'),
        ('miles', 'Miles'),
        ('umbre', 'Umbre'),
        ('erspa', 'Erspa'),
        ('amersfoort', 'Amersfoort'),
        ('seabook', 'Seabook')
    ]

    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=10, choices=ALL_CATEGORIES)
    brand = models.CharField(max_length=10, choices=ALL_BRANDS)
    numeric_size = models.IntegerField()
    alphabetic_size = models.CharField(max_length=10)
    quantity = models.IntegerField()
    is_featured = models.BooleanField()
