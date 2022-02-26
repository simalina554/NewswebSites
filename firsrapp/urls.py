from django.urls import path
from .views import *

urlpatterns = [
    path('test/', test, name='test'),
    path('', HomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contactus/', contact, name='contact'),
    path('category/<int:category_id>', CategoryViewNews.as_view(extra_context={'title': 'Заголовок категории'}),
         name='category'),
    path('views_news/<int:pk>', ViewNews.as_view(), name='view_news'),
    path('add_news', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', userlogin, name='login'),
    path('logout/', userlogout, name='logout')
]

