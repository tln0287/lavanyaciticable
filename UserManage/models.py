from django.db import models




class Menu(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    menuId = models.IntegerField(null=True, blank=True)
    module_id = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    access_name = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=1)

