from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin as lrg
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .models import *
from .forms import *


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegistration()
    return render(request, 'firsrapp/register.html', {"form": form})


def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'firsrapp/login.html', {"form": form})


def userlogout(request):
    logout(request)
    return redirect('login')


def test(request):
    pass


# def test(request):
# objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7', 'ringo8']
# paginator = Paginator(objects, 2)
# page_num = request.GET.get('page', 1)
# page_objects = paginator.get_page(page_num)
# return render(request, 'firsrapp/test.html', {'page_objects': page_objects})


class HomePage(MyMixin, ListView):
    model = News
    template_name = 'firsrapp/home_news_list.html'
    context_object_name = 'newsAll'
    mixin_prop = 'hello'
    paginate_by = 2

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


def about(request):
    title = 'Страница о Нас! Рады вас приветствовать!'
    content = {'title': title, }
    return render(request, template_name="firsrapp/about.html", context=content)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'djangobekov2022@gmail.com',
                             ['simalina554@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено')
            else:
                messages.error(request, 'Ошибка отправки письма!')

        else:
            messages.error(request, 'Ошибка!')
    else:
        form = ContactForm()

    return render(request, 'firsrapp/contactus.html', {"form": form})


def views_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, "firsrapp/views_news.html", {'news_item': news_item})


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class CreateNews(lrg, CreateView):
    form_class = NewsForm
    model = News
    template_name = 'firsrapp/create_news.html'
    success_url = reverse_lazy('home')
    raise_exception = True
