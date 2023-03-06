from django.contrib import admin
from webapp.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline', 'status', 'category', 'type')
    list_filter = ('id', 'title', 'deadline', 'status', 'category', 'type')
    search_fields = ('title', 'deadline', 'category', 'type')
    fields = ('description', 'title', 'deadline', 'status', 'category', 'type')


admin.site.register(ToDo, ToDoAdmin)
