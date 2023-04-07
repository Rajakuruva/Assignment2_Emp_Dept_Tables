from django.db import models

# Create your models here.

class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=30)
    Loc=models.CharField(max_length=50)

    def __str__(self):
        return str(self.Deptno)

class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=50)
    Job=models.CharField(max_length=50)
    Mgr=models.IntegerField()
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.Ename
