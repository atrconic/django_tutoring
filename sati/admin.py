from django.contrib import admin

from .models import Course, Class, Student, Mentor

admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Mentor)

