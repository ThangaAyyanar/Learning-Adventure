from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('delete/<int:todo_id>',views.delete,name='delete'),
    path('mark_complete/<int:todo_id>',views.mark_complete,name='mark_complete'),
    path('mark_incomplete/<int:todo_id>',views.mark_incomplete,name='mark_incomplete'),
    path('edit/<int:todo_id>',views.edit,name="edit")
]
