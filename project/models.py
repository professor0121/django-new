from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    des = models.TextField()
    image = models.ImageField(upload_to="product_image/")
    created_at =models.DateTimeField(auto_now_add=True)