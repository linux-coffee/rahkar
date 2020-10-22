from django.contrib import admin
from .models import News,About,ContactUs
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # inlines =[ProductFileAdmin]
    list_display = ('title','created','published')
    list_filter = ('created',JDateFieldListFilter),
    list_editable = ('published',)
    prepopulated_fields = {'slug':("title",)}


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','created','status')
    list_filter = ('status',('created',JDateFieldListFilter),)
    search_fields = ('name','email')
admin.site.register(About)
