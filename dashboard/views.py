from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import Associates
from dashboard.serializers import CountrySerializer, SexSerializer, StatusSerializer, AssociateSerializer
import json
from rest_framework import generics

# Create your views here.

class CountryGet(generics.ListAPIView):
    queryset = Associates.objects.all()
    serializer_class = AssociateSerializer

    def get_queryset(self):
        country = self.request.query_params.get('country')
        queryset = Associates.objects.filter(country = country)
        return queryset


class GenderGet(generics.ListAPIView):
    queryset = Associates.objects.all()
    serializer_class = AssociateSerializer

    def get_queryset(self):
        gender = self.request.query_params.get('gender')
        queryset = Associates.objects.filter(gender = gender)
        return queryset


class StatusGet(generics.ListAPIView):
    queryset = Associates.objects.all()
    serializer_class = AssociateSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status')
        queryset = Associates.objects.filter(status = status)
        return queryset
"""
Función para registrar colaboradores
@api_view(['POST'])
def associates_post(request):
    if request.method == 'POST':
        serializer = AssociateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

