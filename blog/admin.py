from django.contrib import admin
from .models import Post
from import_export import resources

class PostResource(resources.ModelResource):

    class Meta:
        model = Post
from import_export.admin import ImportExportModelAdmin


class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    pass
    
admin.site.register(Post,PostAdmin)