from django.db import models
from authentication.models import Users
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class StatusUser(models.Model):
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return self.status

class Contrato(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    signature = models.BooleanField()
    job_title = models.CharField(max_length=25)
    start_date = models.TimeField()
    duration = models.DateField()

    def __str__(self):
        return self.first_name

class Country(models.Model):
    country_colleague = models.CharField(max_length=50)
    def __str__(self):
        return self.country_colleague

class JobTitle(models.Model):
    job_title = models.CharField(max_length=50)
    def __str__(self):
        return self.job_title

class Colleagues(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150, unique=True)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True)
    interbank_key = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    #Llaves fóraneas a tablas: contrato, country, status y job_title
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    status_id = models.ForeignKey(StatusUser, on_delete=models.CASCADE)
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE)