from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='startup'

urlpatterns = [
    path('articles/',views.all_article,name ='all_article'),
    path('courses/',views.courses_index,name='courses_index'),
    path('startup/',views.startup_index,name='startup_index'),
    path('course_register/',views.course_register,name='course_register'),
    path('startup_register/',views.startup_register,name='startup_register'),
    path('<slug:slug>/',views.article_detail,name='article_detail'),
]
