from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

@admin.register(Bills)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
    list_display = ('CAF_Number', 'Customer_Name','Lien_men','Activation_Date','Box_number','OLT','total_balance','Date','txn_id')
    search_fields = ('CAF_Number', 'Customer_Name','Lien_men','Activation_Date','Box_number','OLT','total_balance')
    list_filter = (('Date', DateRangeFilter),'Lien_men','flag')



