from django.urls import path
from . import views



urlpatterns = [
    path(r'',views.homepage,name='homepage'),
    path(r'applyform',views.apply_leave, name ='applyform'),
    
]
