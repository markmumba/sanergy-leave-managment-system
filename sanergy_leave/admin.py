from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Department)
admin.site.register(EmploymentTerm)
admin.site.register(LeaveType)
admin.site.register(Notice)
admin.site.register(Leave)
