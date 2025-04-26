from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('cash', 'Cash'),
        ('checkings', 'Checkings/Giro'),
        ('savings', 'Savings'),
        ('credit_card', 'Credit Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, default='')
    account_id = models.CharField(max_length=50, default='')
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    currency = models.CharField(max_length=3, default='EUR')  # ISO 4217 currency code
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.bank_name})"

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new instance
            self.current_balance = self.opening_balance
        super().save(*args, **kwargs)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class RecurringTransaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    frequency = models.CharField(max_length=50)  # e.g., 'monthly', 'weekly'
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
