from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
 
