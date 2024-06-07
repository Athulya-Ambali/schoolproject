from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User

# Create your models here.

class AdminDetails(AbstractBaseUser):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

# school_management/models.py63

class Course(models.Model):
    course_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.course_name

class Batch(models.Model):
    batch=models.CharField(max_length=100)

    def __str__(self):
        return self.batch
    
    
class Country(models.Model):
    country_name=models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
    
    
class State(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=50)

    def __str__(self):
        return self.state_name
    

class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

    
class Teacher(AbstractBaseUser):
    name = models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    email= models.EmailField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_teacher')
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='batch_teacher')
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)

    USERNAME_FIELD = 'username'
  

    def __str__(self):
        return self.name
    

class Student(User):
    # first_name=models.CharField(max_length=50)   because we use User,and these fields are already inbuilt in user
    # last_name=models.CharField(max_length=50)
    # email=models.CharField(max_length=50)
    # username=models.CharField(max_length=50)
    # password=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    father_name=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='student_course')
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='student_batch')
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.first_name
    



