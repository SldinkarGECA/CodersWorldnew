from django.db import models


class Course(models.Model):
    courseName = models.CharField(max_length=200)
    courseImage = models.ImageField(upload_to='images/')
    courseUrl = models.CharField(max_length=200)
    courseDescription = models.TextField(max_length=1200)
    courseCategory = models.CharField(max_length=120)

    def __str__(self):
        return self.courseName
