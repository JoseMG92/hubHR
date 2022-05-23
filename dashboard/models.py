from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.

class UserStatus(models.Model):
    status = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.status

class Sex(models.Model):
    sex = models.CharField(max_length=20)
    
    def __str__(self):
        return self.sex

class Country(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.country

class JobTitle(models.Model):
    job_title = models.CharField(max_length=50)
    def __str__(self):
        return self.job_title


class Contracts(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    signature = models.BooleanField()
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=True)
    start_date = models.TimeField()
    duration = models.DateField()

    def __str__(self):
        return self.first_name


class Associates(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150, unique=True)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True)
    interbank_key = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    #Llaves fóraneas a tablas: contrato, country, status y job_title
    #contract
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)
    country= models.ForeignKey(Country, on_delete=models.CASCADE)
    status = models.ForeignKey(UserStatus, on_delete=models.CASCADE)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'