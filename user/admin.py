from django.contrib import admin
from .models import UserAccount, UserAddress


admin.site.register(UserAccount)
admin.site.register(UserAddress)
