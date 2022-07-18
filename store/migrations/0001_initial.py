# Generated by Django 3.0.7 on 2022-06-21 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('image_profil', models.ImageField(blank=True, upload_to='photos/supliers')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('image_profil', models.ImageField(blank=True, upload_to='photos/supliers')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(blank=True, upload_to='photos/products')),
                ('stock', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('supplier', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.Supplier')),
            ],
        ),
    ]
