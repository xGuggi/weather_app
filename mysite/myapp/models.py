from django.db import models


class Weather(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=500, null=True)
    temperature = models.IntegerField(null=True)
    description = models.CharField(max_length=500, null=True)
    humidity = models.IntegerField(null=True)
    pressure = models.IntegerField(null=True)
    wind_speed = models.IntegerField(null=True)
    visibility = models.IntegerField(null=True)


