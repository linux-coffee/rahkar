from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    path('news/',views.all_news,name ='all_news'),
    path('search/', views.search, name='search'),
    path('',views.index,name='index'),
    path('contact-us/',views.contact_us,name='contact_us'),
    path('about/',views.about,name='about'),
    path('<slug:slug>/',views.news_detail,name='news_detail'),
    
]