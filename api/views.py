from django.shortcuts import render
from dbapp.models import Employee
from django.views import View
from .serialization import EmpSerialization
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
# Create your views here.


@api_view(['GET','POST'])
def GetEmployee(req):
    if req.method == 'GET':
        emps = Employee.objects.all()
        empserialized_obj = EmpSerialization(emps,many=True)
        return Response(empserialized_obj.data)
    
    if req.method == 'POST':
        empserialized_obj = EmpSerialization(data = req.data)
        if empserialized_obj.is_valid():
            empserialized_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(empserialized_obj.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE','GET'])
def ModifyEmployee(req,pk):
    def getEmployee(pk):
        return Employee.objects.get(empid = pk)
    if req.method == 'GET':
        emp = getEmployee(pk)
        empserialized_obj = EmpSerialization(emp)
        return Response(empserialized_obj.data,status=HTTP_200_OK)
    
    if req.method == 'DELETE':
        emp = getEmployee(pk)
        emp.delete()
        return Response(status=HTTP_200_OK)
    
    if req.method == 'PUT':
        emp = getEmployee(pk)
        empserialized_obj = EmpSerialization(emp,data = req.data)
        if empserialized_obj.is_valid():
            empserialized_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(empserialized_obj.errors,status=HTTP_400_BAD_REQUEST)
        
        