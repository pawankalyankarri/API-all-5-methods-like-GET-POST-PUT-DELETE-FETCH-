from django.shortcuts import render,redirect
from django.views import View
from .models import Department,Employee
# Create your views here.

class Insert(View):
    def get(self,req):
        depts = Department.objects.all()
        return render(req,'dbapp/insert.html',{'depts': depts})
    def post(self,req):
        eid = int(req.POST['eid'])
        ename = req.POST['ename']
        salary = int(req.POST['esal'])
        dept = req.POST['dept']
        dept_info = Department.objects.get(deptid = dept)
        Employee.objects.create(empid = eid,empname =ename,empsalary = salary,department = dept_info)
        return redirect('selecturl')
    
    
class Select(View):
    def get(self,req):
        emps = Employee.objects.all()
        return render(req,'dbapp/select.html',{'emps':emps})
    

class Update(View):
    def get(self,req,pk):
        emp = Employee.objects.get(empid = pk)
        depts = Department.objects.all()
        return render(req,'dbapp/update.html',{'emp':emp,'depts':depts})
    
    def post(self,req,pk):
        empname = req.POST['ename']
        empsalary = int(req.POST['esal'])
        edept = int(req.POST['dept'])
        dept_info = Department.objects.get(deptid = edept)
        Employee(empid = pk,empname = empname,empsalary = empsalary,department = dept_info).save()
        
        return redirect('selecturl')
    
    
class Delete(View):
    def get(self,req,pk):
        Employee.objects.get(empid = pk).delete()
        return redirect('selecturl')
        
        