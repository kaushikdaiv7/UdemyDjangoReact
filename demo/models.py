from django.db import models


# Create your models here.
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    isPublished = models.BooleanField(default=False)
    published = models.DateField(blank=True, null=True, default=None)

    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(BookNumber, null=True,
                                  blank=True, on_delete=models.CASCADE)