
from django import template
from django.db.models import Count

register=template.Library()

from ..models import Post,Comment
from ..models import Tag


@register.simple_tag
def total_posts():
	return Post.published.count()

@register.inclusion_tag('blog/post/last_post.html')
def show_last_posts(count=3):
	if Post.published.count()<count:
		last_posts=Post.published.order_by('-publish')[::]
	else:
		last_posts=Post.published.order_by('-publish')[:count]
	return {'last_posts':last_posts}

#获取最近的文章
@register.assignment_tag
def Show_last_posts(count=3):
	if Post.published.count()<count:
		last_posts=Post.published.order_by('-publish')[::]
	else:
		last_posts=Post.published.order_by('-publish')[:count]
	return last_posts

#获取最近的评论
@register.assignment_tag
def Show_last_comments(count=5):
	if Comment.objects.all().count()<count:
		last_comments=Comment.objects.all().order_by('-created')[::]
	else:
		last_comments=Comment.objects.all().order_by('-created')[:count]
	return last_comments


@register.assignment_tag
def get_tags_count():
	return Tag.objects.all().annotate(total_post=Count('post'))[::]

#获取tag
@register.assignment_tag
def Get_tags_count():
	return Tag.objects.all().annotate(total_post=Count('post'))[::]
