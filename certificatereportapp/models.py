from django.db import models
from adminapp.models import Student


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Reportcard(models.Model):
    stuname = models.ForeignKey(Student, on_delete=models.CASCADE)
    sub1 = models.ForeignKey(Subject, related_name='sub1', on_delete=models.CASCADE)
    mark1 = models.IntegerField()
    sub2 = models.ForeignKey(Subject, related_name='sub2', on_delete=models.CASCADE)
    mark2 = models.IntegerField()
    sub3 = models.ForeignKey(Subject, related_name='sub3', on_delete=models.CASCADE)
    mark3 = models.IntegerField()
    sub4 = models.ForeignKey(Subject, related_name='sub4', on_delete=models.CASCADE)
    mark4 = models.IntegerField()
    sub5 = models.ForeignKey(Subject, related_name='sub5', on_delete=models.CASCADE)
    mark5 = models.IntegerField()
    def get_grade(self, mark):
        if mark >= 90:  # Assuming full marks for each subject is 100, total is 500
            return 'A'
        elif mark >= 80:
            return 'B'
        elif mark >= 70:
            return 'C'
        elif mark >= 60:
            return 'D'
        else:
            return 'F'
    def grades(self):
        return {
            'sub1': self.get_grade(self.mark1),
            'sub2': self.get_grade(self.mark2),
            'sub3': self.get_grade(self.mark3),
            'sub4': self.get_grade(self.mark4),
            'sub5': self.get_grade(self.mark5),
        }
    def total_marks(self):
        return self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
    def total_grade(self):
       total = self.total_marks()
       if 450 <= total <= 500:
          return 'A+'
       elif 400 <= total < 450:
          return 'A'
       elif 350 <= total < 400:
          return 'B'
       elif 300 <= total < 350:
          return 'C'
       else:
          return 'F'
    def performance(self):
        grade = self.total_grade()
        if grade in ['A+', 'A']:
           return 'Excellent'
        elif grade == 'B':
           return 'Good'
        elif grade == 'C':
           return 'Average'
        else:
           return 'Poor'
    def __str__(self):
        grades = self.grades()
        total = self.total_marks()
        total_grade = self.total_grade()
        performance = self.performance()
        return (
            f'{self.stuname} - '
            f'{self.sub1.name}: {grades["sub1"]}, '
            f'{self.sub2.name}: {grades["sub2"]}, '
            f'{self.sub3.name}: {grades["sub3"]}, '
            f'{self.sub4.name}: {grades["sub4"]}, '
            f'{self.sub5.name}: {grades["sub5"]}, '
            f'Total Marks: {total}, '
            f'Overall Grade: {total_grade}, '
            f'Performance: {performance}'
        )