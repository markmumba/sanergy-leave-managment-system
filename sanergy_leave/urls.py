from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('apply_leave/',views.apply_leave, name ='apply_leave'),
    path('managersite/',views.managersite , name='managersite' ),
    path('addEmployee',views.addEmployee , name='addEmployee' ),
    path('accept_leave/<int:pk>/',views.accept_leave,name='accept_leave'),
    path('decline_leave/<int:pk>/',views.decline_leave,name='decline_leave'),
   

    # path(r'table',views.append_to_table,name='table') 
]
