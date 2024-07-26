from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User
from django.core.cache import cache

# Create your models here.

class AdminDetails(AbstractBaseUser):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

# school_management/models.py63

class Course(models.Model):
    course_name=models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete('view_course')  # Clear the cache when a course is saved
    
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
    username=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    email= models.EmailField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_teacher')
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='batch_teacher')
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)



    USERNAME_FIELD = 'username'
  

    def __str__(self):
        return self.name
    


class Student(User):
    # first_name=models.CharField(max_length=50)   because we use User,and these fields are already inbuilt in user
    # last_name=models.CharField(max_length=50)
    # email=models.CharField(max_length=50)
    # username=models.CharField(max_length=50)
    # password=models.CharField(max_length=50)
    dob = models.DateField(db_index=True)
    gender = models.CharField(max_length=20, db_index=True)
    mobile = models.CharField(max_length=20, db_index=True)
    address = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50, db_index=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_course', db_index=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='student_batch', db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=['dob']),
            models.Index(fields=['gender']),
            models.Index(fields=['mobile']),
            models.Index(fields=['father_name']),
            models.Index(fields=['course']),
            models.Index(fields=['batch']),
            models.Index(fields=['country']),
            models.Index(fields=['state']),
            models.Index(fields=['city']),
        ]

    



