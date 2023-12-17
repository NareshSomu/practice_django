from django.db import models

class Booking(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    guest_count=models.IntegerField()
    reservation_tine=models.DateTimeField(auto_now=True)
    comments=models.CharField(max_length=1000)

# Create your models here.
