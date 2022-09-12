
from dataclasses import fields
from rest_framework import serializers
from . models import *








class townSerializer(serializers.ModelSerializer):
    class Meta:
        model= Town
        fields= ['town_name','town_code','town_population','city_name']



class citySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = ['city_name','city_area','city_population','state']





class stateSerializer(serializers.ModelSerializer):
    city_state = citySerializer(read_only=True, many=True)
    class Meta:
        model= State
        fields = ['State_name','number_of_cities','number_of_schools','number_of_stadiums','city_state',]
