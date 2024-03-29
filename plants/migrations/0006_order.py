# Generated by Django 4.2.11 on 2024-03-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_rename_dicount_cart_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('credit_card_number', models.CharField(max_length=16)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
            ],
        ),
    ]
