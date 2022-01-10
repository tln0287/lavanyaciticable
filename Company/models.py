from django.db import models
from django.utils import timezone


class Agents(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    agent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    username = models.CharField(max_length=60,null=True, blank=True)
    password = models.CharField(max_length=60,null=True, blank=True)
    mobile = models.CharField(max_length=15,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    status = models.IntegerField(default=0,null=True)
    class Meta:
        verbose_name_plural = "Agents"



class Companys(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    mobile = models.CharField(max_length=15,null=True, blank=True)
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60,null=True, blank=True)
    status = models.IntegerField(default=0,null=True)
    
    class Meta:
        verbose_name_plural = "Companys"
        
class Agent_monthly_collection(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    agent_name = models.CharField(max_length=255,null=True, blank=True)
    date = models.CharField(max_length=255,null=True, blank=True)
    total_cash_collected = models.CharField(max_length=255,null=True, blank=True)
    total_phonepe_collected = models.CharField(max_length=255,null=True, blank=True)
    total_gpay_collected = models.CharField(max_length=255,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Agent_monthly_collection"        
 
   
   





