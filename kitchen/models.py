from django.db import models

class FoodMenu(models.Model):
    name = models.CharField(max_length=100,unique=True)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="kitchen_images")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
