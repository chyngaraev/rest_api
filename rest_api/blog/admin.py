from django.contrib import admin
from .models import Post as PostAdmin
from .models import PostComments as PostCommentsAdmin

# Register your models here.

admin.site.register(PostAdmin)
admin.site.register(PostCommentsAdmin)

