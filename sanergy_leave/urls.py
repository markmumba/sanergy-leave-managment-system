from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('apply_leave/',views.apply_leave, name ='apply_leave'),
    path('managersite/',views.managersite , name='managersite' ),
    path('addEmployee',views.addEmployee , name='addEmployee' ),
   

    # path(r'table',views.append_to_table,name='table') 
]
