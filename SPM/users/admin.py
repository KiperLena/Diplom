from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'phone')



admin.site.register(Account, AccountAdmin)


