from dataclasses import fields
from rest_framework import serializers
from dashboard.models import Associates, Country, Gender, UserStatus

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associates
        fields = ['country','first_name','gender','status']
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country']

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender']
    
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ['status']