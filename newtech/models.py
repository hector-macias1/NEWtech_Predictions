from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_id = models.CharField(max_length=50)
    weight = models.FloatField()
    fat_content = models.CharField(max_length=50)
    visibility = models.FloatField()
    item_type = models.CharField(max_length=50)
    mrp = models.FloatField()

    def __str__(self):
        return self.item_id

class Outlet(models.Model):
    outlet_id = models.CharField(max_length=50)
    establishment_year = models.IntegerField()
    size = models.CharField(max_length=50)
    location_type = models.CharField(max_length=50)
    outlet_type = models.CharField(max_length=50)

    def __str__(self):
        return self.outlet_id

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    sale_amount = models.FloatField()

    def __str__(self):
        return f"Sale of {self.item.item_id} at {self.outlet.outlet_id}"

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item_mrp = models.FloatField()
    outlet_ID = models.CharField(max_length=50)
    outlet_size = models.CharField(max_length=50)
    outlet_type = models.CharField(max_length=50)
    outlet_establishment_year = models.IntegerField()

    min_sales_prediction = models.FloatField()
    max_sales_prediction = models.FloatField()
    is_profitable = models.BooleanField()

    def __str__(self):
        return f"Prediction by {self.user.username} for {self.item.item_id} at {self.outlet.outlet_id}"
