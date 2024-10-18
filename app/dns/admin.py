from django.contrib import admin

from .models import Domain, Record


admin.site.register([
    Domain, Record,
])
