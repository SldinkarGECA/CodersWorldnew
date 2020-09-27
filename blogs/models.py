from django.db import models
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default="")
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=150)
    timestamp = models.DateTimeField(blank=True) 
    
    def __str__(self):
        return self.title + ' by ' + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.CharField(max_length=255,default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "...  by " + str(self.user)  + " on " + str(self.timestamp)