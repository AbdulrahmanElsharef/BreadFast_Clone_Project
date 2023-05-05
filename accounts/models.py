from django.db import models
from django.contrib.auth.models import User
from utils.generate import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile', null=True, blank=True, default='default.png')
    code = models.CharField(max_length=8, default=generate_code)
    phone = models.CharField(_("phone"), max_length=20)
    city = models.CharField(_("city"), max_length=20)
    region = models.CharField(_("region"), max_length=20)
    street = models.CharField(_("street"), max_length=20)
    apartment = models.CharField(_("apartment"), max_length=20)
    Postcode_ZIP = models.CharField(_("Postcode_ZIP"), max_length=20)
    notes = models.CharField(_("notes"), max_length=200)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
