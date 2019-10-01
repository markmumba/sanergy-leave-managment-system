from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('applyform',views.apply_leave, name ='applyform'),
    path('adminsite',views.admin , name='admin' ),
    path('addEmployee',views.addEmployee , name='addEmployee' ),

    # path(r'table',views.append_to_table,name='table') 
]
