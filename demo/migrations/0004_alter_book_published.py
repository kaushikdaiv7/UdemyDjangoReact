# Generated by Django 4.2.6 on 2023-10-23 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_book_cover_book_description_book_ispublished_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]