# Generated by Django 4.0.6 on 2022-07-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20220622_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
