from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    isPublished = models.BooleanField(default=False)
    published = models.DateField(blank=True, null=True, default=None)

    cover = models.ImageField(upload_to='covers/', blank=True)