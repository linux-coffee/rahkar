from django.contrib import admin
from .models import Courses,CourseRegister,Startup,StartupRegister,Article
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title','created','published')
    list_filter = ('title',('created',JDateFieldListFilter),)
    list_editable = ('published',)
    search_fields = ('title',)

@admin.register(CourseRegister)
class CourseRegisterAdmin(admin.ModelAdmin):
    list_display = ('name','family','course','uni_name','phone')
    list_filter = ('name','course','family')
    search_fields = ('name','family','meli_code')

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('title','created','published')
    list_filter = ('title',('created',JDateFieldListFilter),)
    list_editable = ('published',)
    search_fields = ('title',)

@admin.register(StartupRegister)
class StartupRegisterAdmin(admin.ModelAdmin):
    list_display = ('name','how_startup','idea_name','uni_name','phone')
    list_filter = ('name','how_startup')
    search_fields = ('name','idea_name')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','published','subject','created')
    list_filter = ('subject',('created',JDateFieldListFilter),)
    search_fields = ('title',)
    list_editable = ('published',)