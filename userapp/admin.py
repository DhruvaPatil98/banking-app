from django.contrib import admin
from userapp.models import Account , User

# Register your models here.

class AccountInLine(admin.StackedInline):
    model = Account
    max_num = 3

class UserAdmin(admin.ModelAdmin):
  inlines = [AccountInLine]

admin.site.register(User , UserAdmin)