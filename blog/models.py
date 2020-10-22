from django.db import models
from django_jalali.db import models as jmodels
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


STATUS_CONTACT=[
    
    ('f','فوری'),
    ('m','معمولی'),
]

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    text = RichTextUploadingField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'news')
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    def get_absolute_url(self):
        return reverse('blog:news_detail',args=[self.slug])

    def __str__(self):
        return self.title


class About(models.Model):

    description = RichTextUploadingField()

    class Meta:
        ordering = ('description',)
        verbose_name = 'درباره'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.description

class ContactUs(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=30,verbose_name='ایمیل')
    phone = models.CharField(max_length=20,blank=True,verbose_name='تلفن تماس')
    status = models.CharField(choices=STATUS_CONTACT,max_length=1,verbose_name='میزان اهمیت')
    description = models.TextField(verbose_name='متن درخواست')
    created = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس ها'

    def __str__(self):
        return self.name