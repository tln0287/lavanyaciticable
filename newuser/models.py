from django.db import models

# Create your models here.
class Agent_splicings(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    agent_id = models.IntegerField(null=True, blank=True)
    agent_name= models.CharField(max_length=255,null=True, blank=True)
    no_of_splicings = models.IntegerField(null=True, blank=True)
    splicing =  models.CharField(max_length=255,default="0", blank=True)
    area_name = models.CharField(max_length=255,null=True, blank=True)
    
    
    class Meta:
        db_table = 'Agent_splicings'
    
class User_cable_connections(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    connection_type = models.CharField(max_length=255,null=True, blank=True)
    caf_no= models.CharField(max_length=255,null=True, blank=True)
    mobile_no = models.CharField(max_length=255,null=True, blank=True)
    amount_paid = models.CharField(max_length=255,null=True, blank=True)
    
    
    class Meta:
        db_table = 'User_cable_connections'   
    
    
    