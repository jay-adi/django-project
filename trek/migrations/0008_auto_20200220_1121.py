# Generated by Django 3.0.2 on 2020-02-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0007_auto_20200218_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='upi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('transid', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='trek',
            field=models.CharField(choices=[('kedarkantha', 'kedarkantha'), ('chopta/tungnath/deoriya tal', 'chopta/tungnath/deoriya tal'), ('Devkyara', 'Devkyara'), ('Har Ki Doon', 'Har Ki Doon'), ('Parashar Lake,Mandi', 'Parashar Lake,Mandi'), ('Karthik Swami', 'Karthik Swami')], max_length=120),
        ),
    ]