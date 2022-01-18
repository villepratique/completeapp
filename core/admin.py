from django.contrib import admin

from core.models import User
# Register your models here.
admin.site.site_header = "Ma ville pratique Administration"
admin.site.site_title = "Ma ville pratique Admin Portal"
admin.site.index_title = "Welcome to Mavillepratique Researcher Portal"

admin.site.register(User)