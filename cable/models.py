from django.db import models

# Create your models here.


class Bills(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    CAF_Number = models.CharField(max_length=255, null=True, blank=True)
    Customer_Name = models.CharField(max_length=255, null=True, blank=True)
    Customer_Mobile = models.CharField(max_length=255, null=True, blank=True)
    Activation_Date = models.CharField(max_length=255, null=True, blank=True)
    Billing_amount = models.CharField(max_length=255, null=True, blank=True)
    OLT = models.CharField(max_length=255, null=True, blank=True)
    PON = models.CharField(max_length=255, null=True, blank=True)
    Box_number = models.CharField(max_length=255, null=True, blank=True)
    Balance_till_last_month = models.CharField(max_length=255, null=True, blank=True)
    paid = models.CharField(max_length=255, null=True, blank=True)
    Lien_men = models.CharField(max_length=255, null=True, blank=True)
    Date =models.CharField(max_length=255, null=True, blank=True)
    total_balance = models.CharField(max_length=255, null=True, blank=True)
    CAF_Type = models.CharField(max_length=255, null=True, blank=True)
    Base_Package = models.CharField(max_length=255, null=True, blank=True)
    Status  = models.CharField(max_length=255, null=True, blank=True)
    Billing_Frequency  = models.CharField(max_length=255, null=True, blank=True)
    txn_id =  models.CharField(max_length=255, null=True, blank=True)
    flag = models.IntegerField(default=0,null=True)
    Time = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Bills"





