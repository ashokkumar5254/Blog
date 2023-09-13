from django.contrib import admin
from .models import PostModel,comment
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author',)
# Register your models here.
admin.site.register(PostModel,PostAdmin)
admin.site.register(comment)
