
from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models

# Create your models here.



class State(models.Model):
    State_name = models.CharField(primary_key=True,max_length=20)
    number_of_cities = models.IntegerField()
    number_of_schools = models.IntegerField()
    number_of_stadiums = models.IntegerField()
    state_image = models.ImageField(upload_to="static/media",blank = True , null = True)

    def __str__(self):
        return self.State_name

    



class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE, related_name="city_state")
    city_name = models.CharField(max_length=20)
    city_area = models.IntegerField()
    city_population = models.IntegerField()

    def __str__(self):
        return self.city_name


class Town(models.Model):
    city_name = models.ForeignKey(City, on_delete=models.CASCADE, related_name="town_city")
    town_name= models.CharField(max_length=20)
    town_code = models.IntegerField()
    town_population = models.IntegerField()

    def __str__(self):
        return self.town_name


