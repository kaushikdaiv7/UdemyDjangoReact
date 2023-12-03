from django.contrib import admin
from .models import Book, BookNumber


# Register your models here.
admin.site.register(Book)
admin.site.register(BookNumber)
