from django.contrib import admin
from .models import StudentApplying,AcademicApplying, businessEntApplying,Government
# Register your models here.
admin.site.register(StudentApplying)
admin.site.register(AcademicApplying)
admin.site.register(businessEntApplying)
admin.site.register(Government)

