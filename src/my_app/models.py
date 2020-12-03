import random
import string
from django.db import models


# Create your models here.

class Links(models.Model):
    old_link = models.URLField()
    new_linl = models.URLField()
    
    def save(self, *args, **kwargs):
        if not self.new_linl:
            self.new_linl = self.get_url()
        super(Links, self).save(*args, **kwargs)

    def get_url(self):
        current_codes = list(Links.objects.values_list(
            'new_linl', flat=True))
        while True:
            new_linl = self.gen_url()
            if new_linl not in current_codes:
                break
            else:
                continue
        return new_linl

    
    @staticmethod
    def gen_url():
        url = ''
        for i in range(4):
            url += random.choice(string.ascii_lowercase)
        return url