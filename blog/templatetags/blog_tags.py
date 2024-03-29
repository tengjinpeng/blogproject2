from ..models import Post
from django import template
from ..models import Post, Category
from django.db.models.aggregates import Count
from blog.models import Category
from django import template

from ..models import Post, Category
from django.db.models.aggregates import Count
from blog.models import Category
from ..models import Post, Category, Tag

register = template.Library()
@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

from ..models import Post, Category

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)