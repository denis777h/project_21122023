from django.core.paginator import Paginator
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView
)

from .filter import NewsFilter
from .forms import NewsForm
from .models import News


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news_press.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterer'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news_press.html'
    context_object_name = 'news'

    def news_search(request):
        title = request.GET.get('title')
        author = request.GET.get('author')
        date = request.GET.get('date')
        news = News.objects.all()

        if title:
            news = news.filter(title__icontains=title)

        if author:
            news = news.filter(author__icontains=author)

        if date:
            news = news.filter(date__gt=date)

        return render(request, 'news_search.html', {'news': news})



class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_list.html'

    def news_list(request):
        news_list = News.objects.all()
        paginator = Paginator(news_list, 10)  # Display 10 news per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'news_press.html', {'page_obj': page_obj})


s1 = NewsCreate()
s1.news_list()