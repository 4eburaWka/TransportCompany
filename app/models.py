import datetime as datetime
from django.contrib.auth.models import User
from django.db import models


class Dispatcher(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.name}"


class Machine(models.Model):
    model = models.CharField(max_length=50)
    lifting_capacity = models.IntegerField(null=False, blank=False)
    dispatcher = models.ForeignKey(
        Dispatcher, on_delete=models.SET_NULL, related_name="machines", null=True
    )
    
    def __str__(self):
        return f"{self.model}"


class Driver(models.Model):
    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    profile_photo = models.ImageField()

    machine = models.OneToOneField(
        Machine, on_delete=models.SET_NULL, related_name="driver", null=True
    )

    dispatcher = models.ForeignKey(
        Dispatcher, on_delete=models.SET_NULL, related_name="drivers", null=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


class Client(models.Model):
    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, related_name="clients", null=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


class Cargo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, related_name="cargos", null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, related_name="cargos", null=True)
    dispatcher = models.ForeignKey(
        Dispatcher, on_delete=models.SET_NULL, related_name="cargos", null=True
    )

    name = models.CharField(max_length=50)
    weight = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.client.first_name} {self.name}"
