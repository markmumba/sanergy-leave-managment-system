from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('apply_leave',views.apply_leave, name ='apply_leave'),
    path('adminsite',views.admin , name='admin' ),
    path('addEmployee',views.addEmployee , name='addEmployee' ),
    path('api/leave/',views.LeaveList.as_view())

    # path(r'table',views.append_to_table,name='table') 
]
