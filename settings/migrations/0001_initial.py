# Generated by Django 4.2 on 2023-05-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('logo', models.ImageField(default='default.png', upload_to='Company', verbose_name='logo')),
                ('slogan', models.CharField(max_length=50, verbose_name='slogan')),
                ('Email', models.URLField(verbose_name='Email')),
                ('Phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('Address', models.CharField(max_length=500, verbose_name='Address')),
                ('Open_time', models.CharField(max_length=200, verbose_name='Open_time')),
                ('fa_link', models.URLField(verbose_name='facebook')),
                ('tw_link', models.URLField(verbose_name='twitter')),
                ('inst_link', models.URLField(verbose_name='instagram')),
                ('gm_link', models.URLField(verbose_name='gmail')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('fee', models.FloatField(verbose_name='fee')),
            ],
        ),
    ]
