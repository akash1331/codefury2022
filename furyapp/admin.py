from django.contrib import admin
from .models import *

# Register your models here.
class startupdataAdminSite(admin.ModelAdmin):
    list_display = ('company_name','sector','contact_no','team','website')


admin.site.register(investors)
admin.site.register(startup_data,startupdataAdminSite)
admin.site.register(startup_post)
admin.site.register(tasks)
admin.site.register(startup_user)

    