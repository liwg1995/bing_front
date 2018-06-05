from django.db import models

# Create your models here.

from django.db import models
# from django.urls import

class Bing(models.Model):
    id = models.AutoField(primary_key=True)
    dates = models.DateField()
    bing_url = models.CharField(max_length=10000)
    qiniu_url = models.CharField(max_length=10000)
    image_name = models.CharField(max_length=1000)
    # country = models.CharField(max_length=1000)

    def __str__(self):
        return self.bing_url
