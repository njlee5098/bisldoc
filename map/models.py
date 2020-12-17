from django.db import models


# Create your models here.

class Hospital(models.Model):
    encoded_id = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=50)
    type_code = models.IntegerField()
    type_name = models.CharField(max_length=50)
    city_code = models.IntegerField()
    city_name = models.CharField(max_length=50)
    district_code = models.IntegerField()
    district_name = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    foundation_date = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    total_doctor_num = models.IntegerField()
    doctor_num = models.IntegerField()
    intern_num = models.IntegerField()
    resi_num = models.IntegerField()
    board_num = models.IntegerField()

    def __str__(self):
        return self.encoded_id


class Device(models.Model):
    encoded_id = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=50)
    device_code = models.IntegerField()
    device_name = models.CharField(max_length=50)
    device_num = models.IntegerField()

    def __str__(self):
        return self.encoded_id
