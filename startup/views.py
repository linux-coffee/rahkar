from django.shortcuts import render,get_object_or_404
from .models import CourseRegister,Courses,StartupRegister,Startup,Article
from .form import CourseRegisterForm,StartupRegisterForm
from django.contrib import messages
from blog.models import News

def courses_index(request):
    courses = Courses.objects.filter(published = True)
    all_news = News.objects.filter(published = True)
    all_article = Article.objects.filter(subject='c')[:5]
    all_course = Courses.objects.filter(published=True)
    return render(request,'startup/courses_index.html',{'courses' : courses,'all_news':all_news,'all_article':all_article,'all_course':all_course})

def course_register(request):
    all_article = Article.objects.filter(published=True)[:4]
    all_course = Courses.objects.filter(published=True)
    all_news = News.objects.filter(published = True)
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'ثبت نام شما با موفقیت انجام شد','success')
    else:
        form = CourseRegisterForm()
        messages.error(request,'لطفا اطلاعات خواسته شده را با دقت تکمیل نمایید','danger')
    return render(request,'startup/course_register.html',{'form':form,'all_article':all_article,'all_news':all_news,'all_course':all_course})

def startup_index(request):
    all_startup = Startup.objects.filter(published = True)
    all_course = Courses.objects.filter(published=True)
    all_news = News.objects.filter(published = True)
    all_article = Article.objects.filter(subject='s')[:5]
    return render(request,'startup/startup_index.html',{'all_startup' : all_startup,'all_news':all_news,'all_article':all_article,'all_course':all_course})

def startup_register(request):
    all_news = News.objects.filter(published = True)
    all_course = Courses.objects.filter(published=True)
    all_article = Article.objects.filter(subject='s')[:5]
    if request.method == 'POST':
        form = StartupRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'ثبت نام شما با موفقیت انجام شد','success')
    else:
        form = StartupRegisterForm()
        messages.error(request,'لطفا اطلاعات خواسته شده را با دقت تکمیل نمایید','danger')
    return render(request,'startup/startup_register.html',{'form':form,'all_news':all_news,'all_article':all_article,'all_course':all_course})

def article_detail(request,slug):
    all_course = Courses.objects.filter(published=True)
    article = get_object_or_404(Article,slug=slug)
    all_news = News.objects.filter(published = True)
    all_article = Article.objects.filter(subject='s')[:5]
    return render(request,'startup/article_detail.html',{'article':article,'all_news':all_news,'all_article':all_article,'all_course':all_course})