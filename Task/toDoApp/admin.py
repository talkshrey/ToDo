from django.contrib.auth.models import User
from .models import TaskList
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(TaskList)

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'image']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('image', )}),
    )

    add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': ('email','password1', 'password2'),
       }),
   )

    ordering = ('email',)
    filter_horizontal = ()
    

admin.site.register(User, UserAdmin)