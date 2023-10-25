from django.urls import *
from .views import *

urlpatterns=[
    path('',index_view,name="index_url"),
    path('task-creat/', create_task_view, name="create_task_url"),
    path('task-delete/<int:pk>/', delete_task_view, name="delete_task_url"),
    path('task-fininshed/<int:pk>/', finished_task_view, name="finished_task_url"),
    path('status-finished/',finished_view,name="finished_url"),
    path('task-delete/', delete_status_view, name="delete_status_url"),
    path('task-Inprogress/', In_progress_view, name="In_progress_status_url"),
]