from django.db import models

# Create your models here.
class table_rest(models.Model):

    tt = models.CharField(max_length=10,default = 10)
    varr = models.IntegerField(default=33)
    edi = models.CharField(max_length=1000,default='ahmed')

    def __str__(self):
        return self.tt