from django.db import models
from django.contrib.auth.models import AbstractUser


class DebtManager(models.Model):
    loan_type = models.CharField(max_length=100)
    loan_amount = models.IntegerField()
    due_date = models.DateField()

    def __str__(self):
        return self.loan_type


class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    upi_id = models.CharField(max_length=50)
    pan = models.CharField(max_length=12)


class Contest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    monthly_income = models.IntegerField()
    desired_saving = models.IntegerField()
    payment_count = models.IntegerField(default=0)
    saving = models.IntegerField(default = 0)
    last_updated = models.DateTimeField(auto_now=True)
        