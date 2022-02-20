from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewsForm
from .models import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin as lrg
from django.core.paginator import Paginator
# Create your views here.


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'firsrapp/test.html', {'page_objects': page_objects})


class HomePage(MyMixin, ListView):
    model = News
    template_name = 'firsrapp/home_news_list.html'
    context_object_name = 'newsAll'
    # mixin_prop = 'hello'

    # extra_context = {'title': 'Новости'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        # context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryViewNews(lrg, ListView):
    model = News
    template_name = 'firsrapp/home_news_category.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


# def hello(request):
#     text = """<h1>Welcome</h1>"""
#
#     return HttpResponse(text)


# def index(request):
#     allNews = News.objects.order_by('-created_date')
#     content = {'newsAll': allNews, 'titleInHtml': 'Список всех новостей'}
#     return render(request, template_name="firsrapp/index.html", context=content)


# def get_category(request, category_id):
#     news = News.objects.filter(category=category_id)
#     category = Category.objects.get(pk=category_id)
#     content = {'news': news, 'category': category}
#     return render(request, "firsrapp/category.html", content)


def about(request):
    title = 'Страница о Нас! Рады вас приветствовать!'
    content = {'title': title, }
    return render(request, template_name="firsrapp/about.html", context=content)


def contact(request):
    title = 'Страница для связи с нами'
    content = {'title': title, }
    return render(request, template_name="firsrapp/about.html", context=content)


def views_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, "firsrapp/views_news.html", {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#
#         if form.is_valid():
#             News.objects.create(**form.cleaned_data)
#             return redirect('home')
#
#     else:
#         form = NewsForm()
#
#     return render(request, 'firsrapp/add_news.html', {"form": form})


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class CreateNews(lrg, CreateView):
    form_class = NewsForm
    model = News
    template_name = 'firsrapp/create_news.html'
    success_url = reverse_lazy('home')
    # login_url = '/admin/'
    raise_exception = True
