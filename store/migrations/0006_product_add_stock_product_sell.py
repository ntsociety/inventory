# Generated by Django 4.0.5 on 2022-07-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_addstocks_delete_addstock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sell',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
