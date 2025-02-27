from django.contrib import admin
from .models import Topics, TopicNotes, PastPaper

admin.site.register(Topics)
admin.site.register(TopicNotes)
admin.site.register(PastPaper)