from django.db import models

# Create your models here.
class table_rest(models.Model):

    tt = models.CharField(max_length=10)

    def __str__(self):
        return self.tt