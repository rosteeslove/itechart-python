from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField(max_length=30)
    email = models.EmailField(max_length=30)
    postcode = models.CharField(max_length=10) # tmp workaround
    logo = models.ImageField(upload_to='logos')


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_position = models.CharField(max_length=30)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15) # tmp workaround
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='employee'
    )


class PersonalData(models.Model):
    birth_date = models.DateField()
    address = models.CharField(max_length=60) # tmp workaround (TextField maybe ?)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='data'
    )


class Bank(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField(max_length=30)
    email = models.EmailField(max_length=30)
    company = models.ManyToManyField(
        Company,
        related_name='bank'
    )