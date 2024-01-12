from django.contrib import admin
from django.urls import path
from .views import main,yangilik,contact,categori,lates_news

urlpatterns=[
    path('adminka',main,name="adminka"),
    path('yangilik',yangilik,name="yangilik"),
    path('contact',contact,name="contact"),
    path('categori',categori,name="categori"),
    path('lates',lates_news,name="latest")

]