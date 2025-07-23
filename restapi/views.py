from django.shortcuts import render
from dbapp.models import Employee
from .serializer import MySerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
# Create your views here.
@api_view(['GET','POST'])
def GetEmployee(req):
    if req.method == 'GET':
        emps = Employee.objects.all()
        emp_serialized = MySerializer(emps,many = True)
        return Response(emp_serialized.data)
    
    if req.method == 'POST':
        emp_serialized = MySerializer(data = req.data)
        if emp_serialized.is_valid():
            emp_serialized.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(emp_serialized.errors,status=HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])        
def ModifyEmp(req,pk):
    def getEmp(pk):
        try:
            return Employee.objects.get(empid = pk)
        except Employee.DoesNotExist:
            raise ValidationError('emp does not exist')
    if req.method == 'GET':
        emp_serialized = MySerializer(getEmp(pk))
        
        return Response(emp_serialized.data,status=HTTP_200_OK)
    
    if req.method == 'PUT':
        emp = getEmp(pk)
        emp_serialized = MySerializer(emp,data = req.data)
        if emp_serialized.is_valid():
            emp_serialized.save()
            return Response(status = HTTP_201_CREATED)
        else:
            return Response(emp_serialized.errors,status=HTTP_400_BAD_REQUEST)
        
    if req.method == 'DELETE': 
        getEmp(pk).delete()
        
        return Response(status=HTTP_200_OK)
        
        
        
        
    

        
        