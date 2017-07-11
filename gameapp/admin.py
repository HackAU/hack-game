from django.contrib import admin
from gameapp import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'level', 'level_date')
    list_filter = ('level',)
    search_fields = ('username',)
    ordering = ('level',)




admin.site.register(models.User, admin_class=UserAdmin)