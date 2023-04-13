from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField()
    def __str__(self) -> str:
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    
    def __str__(self) -> str:
        return self.author























    








