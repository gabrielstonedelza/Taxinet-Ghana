from django.contrib import admin

from .models import User

class AdminUsers(admin.ModelAdmin):
    list_display = ['id','email','full_name','phone_number','user_tracker_sim','user_blocked','user_approved','username']

    class Meta:
        model = User

admin.site.register(User,AdminUsers)
