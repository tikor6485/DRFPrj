from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=20)
    year = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.model}-{self.year}'

class Person(models.Model):
    newCar = models.ForeignKey(Car, on_delete= models.CASCADE, null=True)
    newName = models.CharField(max_length=30)
    newAge = models.PositiveIntegerField()
    newEmail = models.EmailField()


    def __str__(self):
        return self.newName
