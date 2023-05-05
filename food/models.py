from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.

class Department(models.Model):
    name=models.CharField(_("name"), max_length=50)
    image=models.ImageField(_("image"), upload_to='Department')
    slug=models.SlugField(_("slug"),null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Department, self).save(*args, **kwargs) # Call the real save() method
    
Availability=(
    ('InStock','InStock'),('Sold','Sold'),('Soon','Soon')
)
class Product(models.Model):
    name=models.CharField(_("name"), max_length=50)
    price=models.FloatField(_("price"),max_length=20)
    image=models.ImageField(_(""), upload_to='Product')
    department=models.ForeignKey(Department, verbose_name=_("Department"),related_name='Product_Department', on_delete=models.CASCADE)
    subtitle=models.CharField(_("subtitle"), max_length=300)
    description=models.TextField(_("description"),max_length=2500)
    information=models.TextField(_("information"),max_length=2500)
    available=models.CharField(_("available"), max_length=50,choices=Availability)
    shipping_days=models.IntegerField(_("shipping"))
    Weight=models.FloatField(_("Weight"))
    slug=models.SlugField(_("slug"),null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Product, self).save(*args, **kwargs) # Call the real save() method
    
class ProductImage (models.Model):
    product=models.ForeignKey(Product, verbose_name=_("product"),related_name='Product_Image' ,on_delete=models.CASCADE)
    image=models.ImageField(_("image"), upload_to='Product' )

    def __str__(self):
        return str(self.product)
    
class ProductReview (models.Model):
    user=models.ForeignKey(User, verbose_name=_("user"),related_name='user_review' ,on_delete=models.SET_NULL,blank=True,null=True)
    product=models.ForeignKey(Product, verbose_name=_("product"),related_name='Product_review' ,on_delete=models.CASCADE)
    rate=models.IntegerField(_("rate"))
    review=models.TextField(_("review"),max_length=1000)
    
    def __str__(self):
        return str(self.user)