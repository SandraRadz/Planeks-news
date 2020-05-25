from django.shortcuts import render

# Create your views here.
from django.views import generic

from news.models import New


class NewsList(generic.ListView):
    queryset = New.objects.filter(status='A').order_by('-pub_date')
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewDetail(generic.DetailView):
    queryset = New.objects.filter(status='A')
    template_name = 'news/new_item.html'
    context_object_name = 'new_item'

