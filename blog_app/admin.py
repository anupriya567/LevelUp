from django.contrib import admin
from .models import Blogpost,Content,Contact,Youtube,BlogComment,Contribute

admin.site.register(Content)
admin.site.register(Contact)
admin.site.register(Youtube)
admin.site.register(BlogComment)
admin.site.register(Contribute)

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)