# Generated by Django 4.2.11 on 2024-03-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_itemdetails_nameproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_product', models.IntegerField()),
                ('Id_user', models.IntegerField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('total', models.FloatField()),
                ('dicount', models.FloatField()),
                ('net', models.FloatField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
