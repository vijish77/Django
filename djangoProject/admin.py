from django.contrib import admin

from djangoProject.models import User, Product


class UserAdmin(admin.ModelAdmin):
    # 'address'
    fields = ['username', 'name', 'email', 'address']
    list_display = ['username', 'name']
    search_fields = ['name']

admin.site.register(User, UserAdmin)


    


