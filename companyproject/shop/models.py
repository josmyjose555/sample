from django.db import models
 
# Create your models here.
class shop(models.Model):

    name=models.CharField(max_length=100)
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    offer=models.BooleanField(default=False)
    def __str__(self):
        return self.name

