from django.db import models
class Grade(models.Model):
    grade_id = models.CharField(max_length=20)
    building = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    def __str__(self):
        return self.grade_id