from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'due_date', 'created_by')
    list_filter = ('status', 'due_date', 'created_at')
    search_fields = ('title', 'description', 'assigned_to__username')
    ordering = ('-created_at',)
    
    # Optional: Make status and assigned_to editable directly from the list
    list_editable = ('status', 'assigned_to')

admin.site.register(Task, TaskAdmin)
