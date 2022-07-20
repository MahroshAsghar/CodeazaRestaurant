from rest_framework import serializers
from .models import FastFood
 
class FastFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model= FastFood
        fields=['id', 'name', 'description']
