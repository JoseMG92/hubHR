from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import DO_NOTHING
from dashboard.models import Gender, JobTitle

# Create your models here.
class Users(AbstractUser):
    """
        Profile user model
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, null=True)
    #job_title = models.CharField(max_length=25)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def get_full_name_user(self):
        return {'full_name': f"{self.first_name} {self.last_name}"}
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



