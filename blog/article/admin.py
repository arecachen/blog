from django.contrib import admin
from article.models import Article, Comment



# Register your models here.
class CommentModelAdmin(admin.ModelAdmin):
    list_display=['article','content']
    #list_display_links=['article']
    list_filter=['article','content']
    search_fields=['content']
    
    class meta:
        model=Comment

admin.site.register(Article)
admin.site.register(Comment,CommentModelAdmin)
#admin.site.register(Comment)
