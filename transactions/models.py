from django.db import models

# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    agent_id = models.IntegerField(default=0, null=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    CAF_Number = models.CharField(max_length=255, null=True, blank=True)
    txn_id = models.CharField(max_length=15,null=True, blank=True)
    customer_mobile = models.CharField(max_length=15,null=True, blank=True)
    customer_name =  models.CharField(max_length=60,null=True, blank=True)
    transaction_type = models.CharField(max_length=60,null=True, blank=True)
    paid_amount = models.CharField(max_length=60,null=True, blank=True)
    balance_amount = models.CharField(max_length=60,null=True, blank=True)
    Date = models.DateField(max_length=255, null=True, blank=True)
    package = models.IntegerField(default=0, null=True, blank=True)
    Time = models.CharField(max_length=255, null=True, blank=True)
    
    

    
class Reports(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    agent_id = models.IntegerField(default=0, null=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    bills_collected = models.CharField(max_length=255, null=True, blank=True)
    amount_collected = models.CharField(max_length=60,null=True, blank=True)
    amount_status = models.CharField(max_length=60,null=True, blank=True)
    comments = models.CharField(max_length=200,null=True, blank=True)
    Date = models.DateField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Reports"

class Agents_transaction_submission(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    agent_id = models.IntegerField(default=0, null=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    bills_collected = models.CharField(max_length=255, null=True, blank=True)
    amount_collected = models.CharField(max_length=60,null=True, blank=True)
    amount_status = models.CharField(max_length=60,null=True, blank=True)
    comments = models.CharField(max_length=200,null=True, blank=True)
    Date = models.DateField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Agents transaction submission"