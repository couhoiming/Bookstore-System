# Generated by Django 3.0.8 on 2020-07-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('data_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('book_id', models.CharField(max_length=20, verbose_name='编号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('price', models.FloatField(verbose_name='价格')),
                ('original', models.CharField(max_length=20, verbose_name='出处')),
                ('image', models.CharField(max_length=75, verbose_name='路径')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('username', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'shop_cart',
            },
        ),
    ]
