from django.db import models
from django_jalali.db import models as jmodels
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

CHOICES = [
    ('u','دانشجو'),
    ('g','فارغ التحصیل'),
    ('s','دانش آموز'),
    ('n','هیچکدام')
]
CHOICES_IDEA = [
    ('r','ثبت شده'),
    ('n','ثبت نشده '),
    ('q','غیره')
]

CHOICES_SUBJECT = [
    ('s','استارتاپ'),
    ('c','آموزشی'),
]


class Courses(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'courses')
    published = models.BooleanField(default=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = 'دوره آموزشی'
        verbose_name_plural = 'دوره های آموزشی'

    def __str__(self):
        return self.title


class CourseRegister(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name='انتخاب دوره')
    name = models.CharField(max_length=100 , verbose_name='نام')
    family = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    father_name = models.CharField(max_length=100, verbose_name='نام پدر')
    meli_code= models.BigIntegerField(verbose_name='کدملی',)
    birthday= models.CharField(max_length=10, verbose_name='تاریخ تولد')
    status = models.CharField(choices=CHOICES,max_length=1, verbose_name='وضعیت تحصیلی')
    reshte = models.CharField(max_length=150, verbose_name='رشته')
    uni_name = models.CharField(max_length=200, verbose_name='نام محل تحصیل')
    phone = models.CharField(max_length=15, verbose_name='تلفن')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    city = models.CharField(max_length=100, verbose_name='استان')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'ثبت نام دوره آموزشی'
        verbose_name_plural = 'ثبت نام دوره های آموزشی'
        
    def __str__(self):
        return self.name

class Startup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'startup')
    published = models.BooleanField(default=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = ' استارتاپ'
        verbose_name_plural = 'استارتاپ ها'

    def __str__(self):
        return self.title


class StartupRegister(models.Model):
    how_startup = models.ForeignKey(Startup,on_delete=models.CASCADE,verbose_name='انتخاب استارتاب')
    name = models.CharField(max_length=100 , verbose_name='نام و نام خانوادگی')
    idea_name = models.CharField(max_length=500 , verbose_name='نام ایده')
    idea_description = models.TextField(verbose_name='شرح ایده')
    idea_status = models.CharField(choices=CHOICES_IDEA,max_length=1, verbose_name='وضعیت ثبت ایده')
    zamine = models.TextField(verbose_name='زمينه های تخصصی ايده')
    tarhe_jadid = models.TextField(verbose_name='طرح جدید در پاسخ به چه نیازی بوده و چه مساله ای را حل می‌کند؟')
    maziat_maayeb = models.TextField(verbose_name='مزایا و معایب طرح را شرح دهید')
    zaman_sakht = models.CharField(max_length=500 , verbose_name='پیش بینی تان از زمان و هزینه مورد نیاز جهت نمونه سازی اولیه چقدر است؟')
    manabe = models.TextField(verbose_name='ماخذ علمی یا منابعی را که به توجیه علمی و فنی طرح کمک می کند، نام ببرید')
    khalaqiat = models.TextField (verbose_name='ابتکار، خلاقیت و نوآوری طرح چيست؟')
    group = models.CharField(max_length=1000,verbose_name='اعضای تیم(در صورت وجود)')
    status = models.CharField(choices=CHOICES,max_length=1, verbose_name='وضعیت تحصیلی')
    reshte = models.CharField(max_length=150, verbose_name='رشته تحصیلی')
    uni_name = models.CharField(max_length=200, verbose_name='نام محل تحصیل')
    phone = models.CharField(max_length=15, verbose_name='تلفن')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    city = models.CharField(max_length=100, verbose_name='استان')
    

    class Meta:
        ordering = ('-name',)
        verbose_name = 'ثبت نام در استارتاپ'
        verbose_name_plural = 'ثبت نام در استارتاپ ها'
        
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    text = RichTextUploadingField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'startappnews')
    published = models.BooleanField(default=True)
    subject = models.CharField(choices=CHOICES_SUBJECT,max_length=1,verbose_name='نوع مقاله')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('startup:article_detail',args=[self.slug])

    def __str__(self):
        return self.title