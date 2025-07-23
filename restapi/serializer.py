from rest_framework import serializers
from dbapp.models import Employee

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields = ['empid','empname','empsalary','department']
        
        