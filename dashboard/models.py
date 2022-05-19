from django.db import models

# Create your models here.
class StatusUser():
    status = models.CharField(max_length=20)

class Contrato():
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    signature = models.BooleanField()
    job_title = models.CharField(max_length=25)
    start_date = models.TimeField()
    duration = models.DateField()

class Country():
    country_colleague = models.CharField(max_length=50)

class JobTitle():
    job_title = models.CharField(max_length=50)

class Colleagues():
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150, unique=True)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True)
    interbank_key = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    #Llaves fóraneas a tablas: contrato, country, status y job_title
    contrato_id = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    status_id = models.ForeignKey(StatusUser, on_delete=models.CASCADE)
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE)