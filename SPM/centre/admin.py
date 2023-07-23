from django.contrib import admin
from .models import Area, Type, Group, Report


class AreaAdmin(admin.ModelAdmin):
    list_display = ('title', 'seria', 'region', 'start', 'stop')
    list_display_links = ('title',)
    list_editable = ('stop',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name', )



class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('field', )
    # list_display_links = ('field', )
    # list_editable = ('area',)



admin.site.register(Area, AreaAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Report, ReportAdmin)

admin.site.site_header = "Админ-панель СПМ"
admin.site.site_title = "Админ-панель СПМ"
