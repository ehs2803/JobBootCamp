from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title_en = models.TextField()
    title_kr = models.TextField()
    detail = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'