from django.contrib import admin
from .models import Subject, GradeLevel, Resource, Comment

admin.site.register(Subject)
admin.site.register(GradeLevel)
admin.site.register(Resource)
admin.site.register(Comment)
