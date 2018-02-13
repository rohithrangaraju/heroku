from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    def __str__(self):
        return self.ticker
class Users(models.Model):
    username = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)
    token = models.CharField(max_length=1000)
    def __str__(self):
        return self.username+' '+self.password
class Subcategory(models.Model):
    sub_category_id = models.IntegerField(primary_key=True)
    sub_category_name = models.CharField(max_length=100)
class Sku(models.Model):
    sku_id = models.IntegerField(primary_key=True)
    sku_description = models.CharField(max_length=500)
class Subcategory_SKU(models.Model):
    sub_category_id = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    sku_id = models.ForeignKey(Sku,on_delete=models.CASCADE)
