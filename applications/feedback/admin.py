from django.contrib import admin
from applications.feedback.models import Like, Rating

admin.site.register(Like)
admin.site.register(Rating)
