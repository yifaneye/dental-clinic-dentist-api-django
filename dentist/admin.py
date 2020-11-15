from django.contrib import admin
from django.contrib.admin.models import LogEntry

from dentist.models import Dentist

admin.site.register(Dentist)
admin.site.register(LogEntry)
