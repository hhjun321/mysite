from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Main(models.Model):
    title_text1 = models.CharField(max_length=20, blank=True)
    title_text2 = models.CharField(max_length=20, blank=True)
    title_text3 = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def delete(self, *args, **kwargs):
        super(Main, self).delete(*args, **kwargs)
   
class MainBanner(models.Model):
    main  = models.ForeignKey(Main)
    banner_text = models.CharField(max_length=200)
    banner_img = models.ImageField(upload_to='main/banner')

    def __str__(self):
        return self.banner_text
    
