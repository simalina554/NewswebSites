from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    # path('', index, name='home'),
    path('about/', about, name='about'),
    path('contactus/', contact, name='contact'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>', CategoryViewNews.as_view(extra_context={'title': 'Заголовок категории'}),
         name='category'),
    # path('views_news/<int:news_id>', views_news, name='views_news'),
    path('views_news/<int:pk>', ViewNews.as_view(), name='views_news'),
    # path('add_news', add_news, name='add_news')
    path('add_news', CreateNews.as_view(), name='add_news')
]
