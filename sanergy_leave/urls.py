from django.urls import path
from . import views



urlpatterns = [
    path(r'',views.homepage,name='homepage'),
    path(r'applyform',views.apply_leave, name ='applyform'),
    path(r'adminsite',views.admin , name='admin' ),
    path(r'admin/addEmployee',views.addEmployee , name='addEmployee' )

    # path(r'table',views.append_to_table,name='table') 
]
