from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Furniture(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    material = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    dimensions = models.CharField(max_length=20)
    weight = models.PositiveIntegerField(default=0)
    stock_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="furniture_image/",  null=True, blank=True)
    is_available = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Discount percentage (0-100)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        """Return price after percentage discount as Decimal (2 dp)."""
        if self.discount and self.discount > 0:
            return (self.price * (Decimal('1') - Decimal(self.discount) / Decimal('100'))).quantize(Decimal('0.01'))
        return self.price

    def __str__(self):
        return f"Furniture name: {self.name} -> Furniture price: {self.price} (discount: {self.discount}%)"
    
