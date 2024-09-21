from django.urls import path
from .views import home
from .views import post
from .views import about
from .views import contact

urlpatterns = [
    path('', home, name="home"),
    path('<int:id>', post, name="post"),    
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
]
