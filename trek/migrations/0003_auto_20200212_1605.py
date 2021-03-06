# Generated by Django 3.0.2 on 2020-02-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0002_auto_20200209_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=200)),
                ('imagee', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='confirm',
            field=models.CharField(default='no', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='trek',
            field=models.CharField(choices=[('1111', 'trek1 -price 12111'), ('2222 ', 'trek2-price 12342'), ('22222 ', 'trek3 price 3r4562')], max_length=120),
        ),
    ]
