from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Company (models.Model):
        name=models.CharField(_("name"), max_length=50)
        logo=models.ImageField(_("logo"), upload_to='Company',default='default.png')
        slogan=models.CharField(_("slogan"), max_length=50)
        Email =models.URLField(_("Email"), max_length=200)
        Phone =models.CharField(_("Phone"), max_length=200)
        Address=models.CharField(_("Address"), max_length=500)
        Open_time=models.CharField(_("Open_time"), max_length=200)
        fa_link=models.URLField(_("facebook"), max_length=200)
        tw_link=models.URLField(_("twitter"), max_length=200)
        inst_link=models.URLField(_("instagram"), max_length=200)
        gm_link=models.URLField(_("gmail"), max_length=200)

        def __str__(self) -> str:
            return  self.name

class DeliveryFee(models.Model):
    name=models.CharField(_("name"), max_length=50)
    fee=models.FloatField(_("fee"))
    
    def __str__(self) -> str:
        return  self.name