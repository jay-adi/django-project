# Generated by Django 3.0.2 on 2020-02-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0014_upi_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='upi',
            name='mobile',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upi',
            name='name',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upi',
            name='confirm',
            field=models.CharField(default='no', max_length=5),
        ),
    ]
