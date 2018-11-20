from django.db import models

class Session(models.Model):
    week        = models.CharField(max_length=10)
    week_start  = models.DateField()
    tuesday     = models.DateField()
    thursday    = models.DateField()
    description =models.CharField(max_length=100)



    def __str__(self):
        return self.week
