from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone
from food.models import Product
from utils.generate import generate_code
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    code = models.CharField(_("code"),max_length=10,default=generate_code)
    order_time = models.DateTimeField(_("order_time"),default=timezone.now)

    def  __str__(self):
        return self.code
        

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,verbose_name='order',related_name='order_Detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='product',related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(_("quantity"),)
    price = models.FloatField(_("price"),)
    
    def  __str__(self):
        return str(self.order)