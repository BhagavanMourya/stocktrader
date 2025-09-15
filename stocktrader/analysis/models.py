from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    market_cap = models.BigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Trade(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    trade_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trade of {self.quantity} shares of {self.stock.symbol} at {self.price_per_unit}"