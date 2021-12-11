from django.contrib import admin

from core.models import User
# Register your models here.
admin.site.site_header = "PROJECT Administration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Researcher Portal"

admin.site.register(User)