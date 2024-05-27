from django.db import models

# Create your models here.

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'supplier'


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="books")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    # discount = models.DecimalField(max_length=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'books'
        indexes = [
            models.Index(fields=['name']),
        ]
    
