from django.db import models

from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def str(self):
        return self.name
ROOM_STATUS = [
    ('available', 'متاحة'),
    ('occupied', 'مشغولة'),
    ('cleaning', 'تحتاج تنظيف'),
    ('maintenance', 'قيد الصيانة'),
]

class Room(models.Model):
    roomid = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    beds = models.IntegerField(max_length=50)
    status = models.CharField(max_length=20, choices=ROOM_STATUS, default='available')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    facilities=models.CharField(max_length=100)

    def str(self):
        return self.roomid
from django.db import models

# Create your models here.
