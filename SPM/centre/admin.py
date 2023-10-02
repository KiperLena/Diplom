from django.contrib import admin
from .models import Area, Type, Group, Report, Department1, Department2, Directorate, Bid



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
    list_display = ('field', 'created', )
    list_display_links = ('field',)
    # list_editable = ('area',)

class Department1Admin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'telephone', 'mobile_phone', 'email', 'office')
    list_display_links = ('full_name', 'post')
    list_editable = ('telephone',)

class Department2Admin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'telephone', 'mobile_phone', 'email', 'office')
    list_display_links = ('full_name', 'post')
    list_editable = ('telephone',)


class DirectorateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'telephone', 'mobile_phone', 'email', 'office')
    list_display_links = ('full_name', 'post')
    list_editable = ('telephone',)


class BidAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'date_completed')
    list_display_links = ('title',)




admin.site.register(Area, AreaAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Department1, Department1Admin)
admin.site.register(Department2, Department2Admin)
admin.site.register(Directorate, DirectorateAdmin)
admin.site.register(Bid, BidAdmin)

admin.site.site_header = "Админ-панель СПМ"
admin.site.site_title = "Админ-панель СПМ"
