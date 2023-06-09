# Generated by Django 4.2 on 2023-05-05 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('image', models.ImageField(upload_to='Department', verbose_name='image')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.FloatField(max_length=20, verbose_name='price')),
                ('image', models.ImageField(upload_to='Product', verbose_name='')),
                ('subtitle', models.CharField(max_length=300, verbose_name='subtitle')),
                ('description', models.TextField(max_length=2500, verbose_name='description')),
                ('information', models.TextField(max_length=2500, verbose_name='information')),
                ('available', models.CharField(choices=[('InStock', 'InStock'), ('Sold', 'Sold'), ('Soon', 'Soon')], max_length=50, verbose_name='available')),
                ('shipping_days', models.IntegerField(verbose_name='shipping')),
                ('Weight', models.FloatField(verbose_name='Weight')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Department', to='food.department', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(verbose_name='rate')),
                ('review', models.TextField(max_length=1000, verbose_name='review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_review', to='food.product', verbose_name='product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Product', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Image', to='food.product', verbose_name='product')),
            ],
        ),
    ]
