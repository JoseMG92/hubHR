
from rest_framework import  serializers
from authentication.models import Users

    

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
   
    
    class Meta:
         model = Users
         fields = ['id', 'username','email', 'first_name', 'last_name', 'job_title','gender']