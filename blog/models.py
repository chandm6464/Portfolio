from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    description=models.TextField()
    
    def summary(self):
        return self.description[:100]    
    
    def dateModify(self):
        return self.pub_date.strftime('%b%e, %Y')
    
    def __str__(self):
        return self.title