# coding: utf-8

from __future__ import unicode_literals

from django.db import models
#from django.urls.base import reverse_lazy

# Create your models here.
class Photo(models.Model):
    image_file = models.ImageField(upload_to='%Y/%m/%d')
    filtered_image_file = models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo, self).delete(*args, **kwargs)
    '''    
    def get_absolute_url(self):
        return reverse_lazy('view_single_photo', kwargs={'photo_id':self.id})
        
    '''
        
