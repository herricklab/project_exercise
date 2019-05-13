# this is required to show the app on admin page

from django.contrib import admin

from .models import Question

admin.site.register(Question)
