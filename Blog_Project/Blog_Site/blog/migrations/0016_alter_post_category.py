# Generated by Django 4.1.1 on 2022-10-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Crypto-Currency', max_length=200),
        ),
    ]
