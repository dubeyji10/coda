from django.db import models
from accounts.models import CustomerUser
from django.utils import timezone

from django.contrib.auth import get_user_model


# Create your models here.


class Payment_Information(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey("accounts.CustomerUser",
        verbose_name=("Client Name"),
        on_delete=models.CASCADE,
        related_name="customer")
    payment_fees=models.IntegerField()
    down_payment=models.IntegerField(default=500)
    student_bonus=models.IntegerField(null=True,blank=True)
    fee_balance=models.IntegerField(default=None)
    plan = models.CharField(max_length=500)
    payment_method = models.CharField(max_length=100)
    contract_submitted_date = models.DateTimeField(default=timezone.now)
    client_signature = models.CharField(max_length=1000)
    company_rep = models.CharField(max_length=1000)
    client_date = models.CharField(max_length=100,null=True,blank=True)
    rep_date = models.CharField(max_length=100,null=True,blank=True)

class Payment_History(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("accounts.CustomerUser",
        verbose_name=("Client Name"),
        on_delete=models.CASCADE,
        related_name="customer_payment_history")
    payment_fees=models.IntegerField()
    down_payment=models.IntegerField(default=500)
    student_bonus=models.IntegerField(null=True,blank=True)
    fee_balance=models.IntegerField(default=None)
    plan = models.CharField(max_length=500)
    payment_method = models.CharField(max_length=100)
    contract_submitted_date = models.DateTimeField(default=timezone.now)
    client_signature = models.CharField(max_length=1000)
    company_rep = models.CharField(max_length=1000)
    client_date = models.CharField(max_length=100,null=True,blank=True)
    rep_date = models.CharField(max_length=100,null=True,blank=True)


class Default_Payment_Fees(models.Model):
	id = models.AutoField(primary_key=True)
	job_down_payment_per_month = models.IntegerField(default=500)
	job_plan_hours_per_month = models.IntegerField(default=40)
	student_down_payment_per_month = models.IntegerField(default=500)
	student_bonus_payment_per_month = models.IntegerField(default=250)


class TrainingLoan(models.Model):
    DEBIT = "Debit"
    CREDIT = "Credit"
    LOAN_CHOICES = [
        (DEBIT, "Debit"),
        (CREDIT, "Credit"),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.CharField(max_length=25, choices=LOAN_CHOICES,)
    value = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
