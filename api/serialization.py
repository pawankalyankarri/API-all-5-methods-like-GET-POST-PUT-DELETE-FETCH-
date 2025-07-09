from rest_framework import serializers
from dbapp.models import Employee
from rest_framework.exceptions import ValidationError

class EmpSerialization(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['empid','empname','empsalary','department']
        
    def validate(self,validated_data):
        if validated_data['empsalary']<0:
            raise ValidationError('salary should not negative')
        if len(validated_data['empname'])<3:
            raise ValidationError('emp name should contain minimum 3 characters')
        
        return validated_data