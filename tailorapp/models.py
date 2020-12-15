from django.db import models
from datetime import datetime
# Create your models here.
class customer(models.Model):
     id=models.AutoField
     name=models.CharField(max_length=20)
     lname=models.CharField(max_length=20)
     phone=models.CharField(max_length=20, default='NOT AVAILABLE', blank=True)
     email = models.CharField(max_length=254, default='NOT AVAILABLE', blank=True)
     shirtunchi=models.DecimalField(max_digits=6, decimal_places=3)
     chest = models.DecimalField(max_digits=6, decimal_places=3)
     shoulder = models.DecimalField(max_digits=6, decimal_places=3)
     astin = models.DecimalField(max_digits=6, decimal_places=3)
     sfront = models.DecimalField(max_digits=6, decimal_places=3)
     coller = models.DecimalField(max_digits=6, decimal_places=3)
     cuf = models.DecimalField(max_digits=6, decimal_places=3)
     pantunchi = models.DecimalField(max_digits=6, decimal_places=3)
     kambar = models.DecimalField(max_digits=6, decimal_places=3)
     sit = models.DecimalField(max_digits=6, decimal_places=3)
     mandi = models.DecimalField(max_digits=6, decimal_places=3)
     gudhga = models.DecimalField(max_digits=6, decimal_places=3)
     bottom = models.DecimalField(max_digits=6, decimal_places=3)
     description = models.CharField(max_length=20, default='not available', blank=True)
     payment = models.CharField(max_length=20, default=0)
     status=models.CharField(max_length=10, default='not completed')
     date = models.DateField(default=datetime.now)

     def __str__(self):
         return self.name+self.lname


