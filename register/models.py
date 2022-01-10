from django.db import models

# Create your models here.

class NewRegister(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    CAF_NO = models.CharField(max_length=255, null=True, blank=True)
    Customer_Name = models.CharField(max_length=255, null=True, blank=True)
    AADHAR_NO = models.CharField(max_length=255, null=True, blank=True) 
    Box_no = models.CharField(max_length=255, null=True, blank=True)
    Activation_date = models.CharField(max_length=255, null=True, blank=True)
    Phone_number = models.CharField(max_length=255, null=True, blank=True)
    Status = models.CharField(max_length=255, null=True, blank=True)    

    def __str__(self):
        return self.CAF_NO
