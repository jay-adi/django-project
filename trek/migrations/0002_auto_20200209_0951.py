# Generated by Django 3.0.2 on 2020-02-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='transid',
            field=models.CharField(default='', max_length=20),
        ),
    ]
