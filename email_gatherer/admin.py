from django.contrib import admin

from .models import GatheredEmail, GatheredEmailAdmin


admin.site.register(GatheredEmail, GatheredEmailAdmin)