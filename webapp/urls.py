from django.urls import path

from webapp.views.todos import edit_view, delete_view, ToDoView, ToDoAddView
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path('add', ToDoAddView.as_view(), name='todo_add'),
    path('edit/<int:pk>', edit_view, name='todo_edit'),
    path('todo/<int:pk>', ToDoView.as_view(), name='todo_view'),
    path('delete/<int:pk>', delete_view, name='todo_delete'),
]