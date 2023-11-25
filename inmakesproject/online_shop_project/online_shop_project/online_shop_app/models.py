from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=230)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
class client(models.Model):
    name=models.CharField(max_length=230)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
