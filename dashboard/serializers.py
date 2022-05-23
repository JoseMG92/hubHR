from dataclasses import fields
from rest_framework import serializers
from dashboard.models import Associates, Country, Sex, UserStatus

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associates
        fields = ['country','first_name','sex','status']
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country']

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ['sex']
    
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ['status']