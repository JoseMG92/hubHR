from dataclasses import fields
from rest_framework import serializers
from dashboard.models import Associates

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associates
        fields = ('first_name', 'last_name','email', 'rfc', 'curp','sex', 'interbank_key','contract','country','status','job_title')

 