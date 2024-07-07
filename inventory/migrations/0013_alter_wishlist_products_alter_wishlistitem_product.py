# Generated by Django 5.0.2 on 2024-03-26 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_wishlist_wishlistitem_wishlist_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='wishlists_new', through='inventory.WishlistItem', to='inventory.productinventory'),
        ),
        migrations.AlterField(
            model_name='wishlistitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wishlists_newss', to='inventory.productinventory'),
        ),
    ]
