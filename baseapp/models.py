from django.db import models


# Create your models here.
class DebtManager(models.Model):
    loan_type = models.CharField(max_length=100)
    loan_amount = models.IntegerField()
    due_date = models.DateField()

    def __str__(self):
        return self.loan_type
