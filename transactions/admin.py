from .models import Transaction,Reports,Agents_transaction_submission
from import_export.admin import ImportExportModelAdmin
from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter



# Register your models here.


@admin.register(Transaction)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ('agent_id', 'Date', 'transaction_type')
    list_filter = (('Date', DateRangeFilter), 'Date', 'agent_name', 'transaction_type')
    list_display = ('CAF_Number','agent_id', 'agent_name', 'Date','Time', 'transaction_type', 'paid_amount','txn_id','package')

    


    
@admin.register(Reports) 

class MyModelAdmin(ModelAdminTotals):
    search_fields = ('agent_id', 'Date', 'agent_name')
    list_filter = (('Date', DateRangeFilter), 'Date', 'agent_name')
    list_display =  ('agent_id', 'Date', 'agent_name', 'amount_collected','comments')
    

@admin.register(Agents_transaction_submission) 
class MyModelAdmin(ModelAdminTotals):
    search_fields = ('agent_id', 'Date', 'agent_name')
    list_filter = (('Date', DateRangeFilter), 'Date', 'agent_name')
    list_display =  ('agent_id', 'Date', 'agent_name', 'amount_collected','comments')



    




