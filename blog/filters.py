import django_filters

from .models import *

class PostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Post
        fields = "__all__"