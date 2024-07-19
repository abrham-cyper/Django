from django.db import models

class info(models.Model):
    number=models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    pop=models.PositiveBigIntegerField()
    area = models.FloatField()
    capitalcity = models.CharField(max_length=100)
    flag =models.ImageField(upload_to='flag')
    email = models.EmailField()
    map = models.ImageField(upload_to='map')
    website = models.URLField()

    def __str__(self):
        return self.name+"------"+self.capitalcity




