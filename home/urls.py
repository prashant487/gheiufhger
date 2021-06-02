from django.urls import path, include
from .views import *
app_name = "home"
urlpatterns = [
    path('', homes, name='home'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    path('blog-home', blog_home, name='blog_home'),
    path('blog-single', blog_single, name='blog_single'),
    path('about', about, name='about'),


]





