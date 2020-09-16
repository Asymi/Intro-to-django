from django.db import models

# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=30)
    # main_ingredient = models.TextField()

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    tastiness = models.PositiveIntegerField()
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name