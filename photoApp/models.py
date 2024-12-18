from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.area}, {self.district}, {self.state}, {self.country}"

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Studio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.CharField(max_length=20)
    employees = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='studios')
    services = models.ManyToManyField(Service, related_name='studios')

    def __str__(self):
        return self.name

    
    
class Photographer(models.Model):
    name = models.CharField(max_length=100)
    license_no = models.CharField(max_length=20)
    experience_in_years = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='photographers')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return f"{self.customer_name} - {self.studio.name} - {self.service.name}"