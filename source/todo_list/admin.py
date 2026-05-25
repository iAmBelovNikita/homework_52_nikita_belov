from django.contrib import admin

from .models import TodoTask

# Register your models here.

class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'status', 'finish_date')
    list_filter = ('status', 'finish_date')
    fields = ('description', 'status', 'finish_date')
    search_fields = ('description', 'status', 'created_at', 'finish_date')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(TodoTask, TodoTaskAdmin)