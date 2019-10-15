from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('apply_leave/',views.apply_leave, name ='apply_leave'),
    path('tableleaves/', views.table, name='table'),
    path('managersite/',views.managersite , name='managersite' ),
    path('addEmployee',views.addEmployee , name='addEmployee' ),
    path('accept_leave/<int:pk>/',views.accept_leave,name='accept_leave'),
    path('decline_leave/<int:pk>/',views.decline_leave,name='decline_leave'),
    path('employee_list/',views.employee_list, name ='employee_list'),
]
