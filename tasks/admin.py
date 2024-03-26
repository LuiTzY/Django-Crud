from django.contrib import admin
from .models import Tasks
# Register your models here.
class tasksConfig(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    search_fields = ("title","description")

admin.site.register(Tasks,tasksConfig)