from __future__ import unicode_literals
import random
import string
from django.db import models

def code_generator(size=6, chars=string.ascii_lowercase + string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))

class SagyURL(models.Model):
    url = models.CharField(max_length = 220)
    shortcode = models.CharField(max_length = 20, unique= True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #empty_datetime = models.DateTimeField(auto_now = False, auto_now_add=False)

    def save(self,*args, **kwargs):
        print("something something")
        self.shortcode = code_generator()
        super(SagyURL, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
