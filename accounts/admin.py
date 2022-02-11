from django.contrib import admin

from accounts.models import Account, MyAccountManager, UserProfile

# Register your models here.

admin.site.register(Account, MyAccountManager, UserProfile)