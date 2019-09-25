from django.urls import path
from . import views



urlpatterns = [
    path(r'',views.homepage,name='homepage'),
    path(r'leavepage',views.leavepage,name='leavepage')
]
