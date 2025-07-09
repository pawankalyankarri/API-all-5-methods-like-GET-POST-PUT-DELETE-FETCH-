from django.db import models

# Create your models here.

class Department(models.Model):
    deptid = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=30)
    deptloc = models.CharField(max_length=30)
    
    def __str__(self):
        return self.deptname


class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=30)
    empsalary = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.empname