from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
