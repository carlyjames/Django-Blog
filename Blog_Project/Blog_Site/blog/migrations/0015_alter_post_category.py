# Generated by Django 4.1.1 on 2022-10-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
    ]
