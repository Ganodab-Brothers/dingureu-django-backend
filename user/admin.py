from django.contrib import admin
from user.models import User, School, RegisterApplication
from user.forms import UserCreationForm

admin.site.register(RegisterApplication)
admin.site.register(School)


class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm

    class RegisterApplicationInline(admin.TabularInline):
        model = RegisterApplication

    inlines = [RegisterApplicationInline]


admin.site.register(User, UserAdmin)