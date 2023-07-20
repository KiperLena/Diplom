from django.contrib import admin
from .models import Area, Type


admin.site.register(Area)
admin.site.register(Type)

admin.site.site_header = "Админ-панель СПМ"
admin.site.site_title = "Админ-панель СПМ"
