from django.db import models


class Homepage(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.title
