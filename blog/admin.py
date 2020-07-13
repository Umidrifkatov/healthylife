from django.contrib import admin
from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',)
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['publish']
admin.site.register(Post, PostAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created',)
    list_filter = ('created',)
    search_fields = ('name', 'body',)
admin.site.register(Comment, CommentAdmin)