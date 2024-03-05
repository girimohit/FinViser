from django.db import models
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     age = models.IntegerField()
#     full_name = models.CharField(max_length=100)
#     phone_number = models.IntegerField()
#     upi_id = models.CharField(max_length=50)
#     pan = models.CharField(max_length=12)


# class CustomUser(AbstractUser):
#     age = models.IntegerField()


class DebtManager(models.Model):
    loan_type = models.CharField(max_length=100)
    loan_amount = models.IntegerField()
    due_date = models.DateField()

    def __str__(self):
        return self.loan_type
