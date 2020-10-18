from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

from address.models import AddressField
from enum import Enum

class PaymentMethods(Enum):
    COD = "Cash On Delivery"
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    UPI = "UPI"
    PAYTM = "Paytm"

# Create your models here.
class User(AbstractUser):
    address = AddressField(blank=True, null=True)
    profile_pic_url = models.CharField(max_length=500, blank=True)
    preferred_payment_option = models.CharField(max_length=30,
                               choices=[(method, method.value) for method in PaymentMethods],
                               default=PaymentMethods.COD)
    wallet_cash = models.DecimalField(max_digits=6, decimal_places=2, default=0,
                                      validators=[MinValueValidator(0)])
