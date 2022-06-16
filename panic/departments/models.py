from django.db import models

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=250)
    rating = models.IntegerField()
    location = models.CharField(max_length=250)

class Police_Station(models.Model):
    station_name = models.CharField(max_length=250)
    rating = models.FloatField()
    location = models.CharField(max_length=250)
    