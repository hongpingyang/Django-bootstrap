from django.contrib import admin
from .models import Post, Comment,Tag
from pagedown.widgets import AdminPagedownWidget
from django import forms

# 定义自己的form
class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    form = PostForm
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',  'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name',  'body')
admin.site.register(Comment, CommentAdmin)

class  TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('name', 'created' )
    search_fields = ('name', 'created')
admin.site.register(Tag,TagAdmin)

    


