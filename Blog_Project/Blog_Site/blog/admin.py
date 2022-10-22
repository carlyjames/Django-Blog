from django.contrib import admin
from blog.models import Post,Comment,Category
from blog.models import SubscribedUser

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

# admin.site.register(CustomUser)
admin.site.register(SubscribedUser, SubscribedUsersAdmin)