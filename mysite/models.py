from django.db import models

# Create your models here.


class Attendee (models.Model):

    fullname = models.CharField(max_length=70)
    email = models.EmailField()
    date1 = models.BooleanField(default=False)
    date2 = models.BooleanField(default=False)
    date1_confirmed = models.DateField(blank=True)
    date2_confirmed = models.DateField(blank=True)

    def __str__(self):
        return self.fullname
