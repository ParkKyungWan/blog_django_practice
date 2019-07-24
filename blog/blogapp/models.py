from django.db import models

# Create your models here.
class Board(models.Model):
    title =models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return "제목: "+self.title