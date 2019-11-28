from django.contrib import admin
from testapp.models import studentmodel

class studentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

# Register your models here.
admin.site.register(studentmodel,studentAdmin)
