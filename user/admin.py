from django.contrib import admin
from user.models import User, School, RegisterApplication

admin.site.register(RegisterApplication)
admin.site.register(School)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class RegisterApplicationInline(admin.TabularInline):
        model = RegisterApplication

    inlines = [RegisterApplicationInline]