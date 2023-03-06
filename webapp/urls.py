from django.urls import path

from webapp.views.todos import delete_view, ToDoView, ToDoAddView, ToDoEditView
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path('add', ToDoAddView.as_view(), name='todo_add'),
    path('edit/<int:pk>', ToDoEditView.as_view(), name='todo_edit'),
    path('todo/<int:pk>', ToDoView.as_view(), name='todo_view'),
    path('delete/<int:pk>', delete_view, name='todo_delete'),
]