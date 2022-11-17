from django.contrib import admin
from .models import User, Subject, Topic, subTopic, StudentData, subTopicData
# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(subTopic)
admin.site.register(StudentData)
admin.site.register(subTopicData)
