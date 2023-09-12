from django.contrib import admin
from .models import Task
# Register your models here.

admin.site.register(Task)

admin.site.site_header = "To Do List By Shariar Rafi >admin"
admin.site.index_title = "Welcome to, To Do List By Shariar Rafi"
admin.site.site_title = "To Do List By Shariar Rafi"