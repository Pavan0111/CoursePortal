from django.db import models

class Courses(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     
   
     content= models.TextField()
     timeStamp=models.DateTimeField(blank=True)


     def __str__(self):
          return self.name 