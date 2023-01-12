from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField()
    
    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   inventory = models.SmallIntegerField()

   def __str__(self):
       return f"{self.title} : {str(self.price)}"