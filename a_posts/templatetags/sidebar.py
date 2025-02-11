from django.db.models import Count
from django.template import Library

from ..models import Tag, Post, Comment

register = Library()

@register.inclusion_tag('includes/sidebar.html')
def sidebar_view(tag=None, user=None):
    top_posts = Post.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')[:5]
    top_comments = Comment.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')[:5]
    categories = Tag.objects.all()
    context = {
        "categories": categories,
        "tag": tag,
        "top_posts": top_posts,
        "top_comments": top_comments,
        "user": user
    }
    return context

