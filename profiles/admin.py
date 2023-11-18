from django.contrib import admin


from .models import Profile

class AdminProfile(admin.ModelAdmin):
    list_display = ['id','user','profile_pic','date_created']
    class Meta:
        model = Profile

admin.site.register(Profile,AdminProfile)
