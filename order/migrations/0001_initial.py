# Generated by Django 4.2 on 2023-05-05 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.generate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=utils.generate.generate_code, max_length=10, verbose_name='code')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='order_time')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('price', models.FloatField(verbose_name='price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_Detail', to='order.order', verbose_name='order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_product', to='food.product', verbose_name='product')),
            ],
        ),
    ]
