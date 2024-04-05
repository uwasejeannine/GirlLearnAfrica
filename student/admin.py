from django.contrib import admin
from .models import Student, Mentor, Feedback, Course, CommunityEvent

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Feedback)
admin.site.register(Course)
admin.site.register(CommunityEvent)
