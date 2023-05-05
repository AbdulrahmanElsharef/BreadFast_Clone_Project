from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils import timezone
from taggit.managers import TaggableManager
from food.models import Department

# Create your models here.

class Post (models.Model):
    author=models.ForeignKey(User, verbose_name=_("author"),related_name='post_author', on_delete=models.SET_NULL,null=True,blank=True)
    department=models.ForeignKey(Department, verbose_name=_("department"),related_name='post_department', on_delete=models.SET_NULL,null=True,blank=True)
    date=models.DateTimeField(_("date"), default=timezone.now)
    image=models.ImageField(_("image"), upload_to='post')
    title=models.CharField(_("title"), max_length=50)
    head_topic=models.CharField(_("head_topic"), max_length=300)
    post=models.TextField(_("post"),max_length=2500)
    Tag=TaggableManager()
    slug=models.SlugField(_("slug"),null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs) # Call the real save() method
    
        
