from django.shortcuts import render,get_object_or_404
from .models import News,About,ContactUs
from startup.models import Article,Courses,Startup
from .forms import ContactUsForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.db.models import Q

def index(request):
    all_news = News.objects.filter(published=True)[:4]
    all_article = Article.objects.filter(published=True)[:4]
    all_startup = Startup.objects.filter(published = True)
    all_course = Courses.objects.filter(published=True)
    return render(request,'blog/index.html',{'all_news':all_news,'all_startup':all_startup,'all_article' : all_article,'all_course':all_course})

def about(request):
    all_news = News.objects.filter(published=True)[:4]
    all_article = Article.objects.filter(published=True)[:4]
    all_course = Courses.objects.filter(published=True)
    about = About.objects.all()
    return render(request,'blog/about.html',{'all_news':all_news,'all_article' : all_article,'all_course':all_course,'about':about})

def contact_us(request):
    all_news = News.objects.filter(published=True)[:4]
    all_article = Article.objects.filter(published=True)[:4]
    all_course = Courses.objects.filter(published=True)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'درخواست شما با موفقیت ارسال شد','success')
    else:
        form = ContactUsForm()
        messages.error(request,'لطفا اطلاعات خواسته شده را با دقت تکمیل نمایید','danger')
    return render(request,'blog/contact_us.html',{'all_news':all_news,'all_article' : all_article,'all_course':all_course,'form':form})

def news_detail(request,slug):
    all_news = News.objects.filter(published=True)[:4]
    news = get_object_or_404(News,slug=slug)
    all_article = Article.objects.filter(published=True)[:4]
    all_course = Courses.objects.filter(published=True)
    return render(request,'blog/news_detail.html',{'news':news,'all_article' : all_article,'all_news':all_news,'all_course':all_course})

def all_news(request):
    all_news = News.objects.filter(published=True)
    all_article = Article.objects.filter(published=True)[:4]
    all_course = Courses.objects.filter(published=True)
    return render(request,'blog/all_news.html',{'all_news':all_news,'all_article' : all_article,'all_course':all_course})

def search(request):
        all_news = News.objects.filter(published=True)
        all_article = Article.objects.filter(published=True)[:4]
        all_course = Courses.objects.filter(published=True)
        if request.method == 'GET':
            query = request.GET.get('q')
            object_list = News.objects.filter(
                Q(title__icontains=query)|Q(text__icontains=query)
            )
        return render(request,'blog/search.html',{'all_news':all_news,'all_article' : all_article,'all_course':all_course,'object_list':object_list})