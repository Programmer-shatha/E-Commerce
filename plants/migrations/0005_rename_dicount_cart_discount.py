# Generated by Django 4.2.11 on 2024-03-07 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_cart_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='dicount',
            new_name='discount',
        ),
    ]
