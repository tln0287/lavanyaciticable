from django.contrib import admin
from .models import Agents, Companys
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Companys)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('name', 'mobile')
    search_fields = ('name', 'mobile')

@admin.register(Agents)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('agent_id', 'name', 'mobile')
    search_fields = ('agent_id', 'name', 'mobile')




