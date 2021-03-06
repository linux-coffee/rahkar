# Generated by Django 3.1.1 on 2020-10-09 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='courses')),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'دوره آموزشی',
                'verbose_name_plural': 'دوره های آموزشی',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='startup')),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': ' استارتاپ',
                'verbose_name_plural': 'استارتاپ ها',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='StartupRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('idea_name', models.CharField(max_length=500, verbose_name='نام ایده')),
                ('idea_description', models.TextField(verbose_name='شرح ایده')),
                ('idea_status', models.CharField(choices=[('r', 'ثبت شده'), ('n', 'ثبت نشده '), ('q', 'غیره')], max_length=1, verbose_name='وضعیت ثبت ایده')),
                ('zamine', models.TextField(verbose_name='زمينه های تخصصی ايده')),
                ('tarhe_jadid', models.TextField(verbose_name='طرح جدید در پاسخ به چه نیازی بوده و چه مساله ای را حل می\u200cکند؟')),
                ('maziat_maayeb', models.TextField(verbose_name='مزایا و معایب طرح را شرح دهید')),
                ('zaman_sakht', models.CharField(max_length=500, verbose_name='پیش بینی تان از زمان و هزینه مورد نیاز جهت نمونه سازی اولیه چقدر است؟')),
                ('manabe', models.TextField(verbose_name='ماخذ علمی یا منابعی را که به توجیه علمی و فنی طرح کمک می کند، نام ببرید')),
                ('khalaqiat', models.TextField(verbose_name='ابتکار، خلاقیت و نوآوری طرح چيست؟')),
                ('group', models.CharField(max_length=1000, verbose_name='اعضای تیم(در صورت وجود)')),
                ('status', models.CharField(choices=[('u', 'دانشجو'), ('g', 'فارغ التحصیل'), ('s', 'دانش آموز'), ('n', 'هیچکدام')], max_length=1, verbose_name='وضعیت تحصیلی')),
                ('reshte', models.CharField(max_length=150, verbose_name='رشته تحصیلی')),
                ('uni_name', models.CharField(max_length=200, verbose_name='نام محل تحصیل')),
                ('phone', models.CharField(max_length=15, verbose_name='تلفن')),
                ('email', models.EmailField(max_length=150, verbose_name='ایمیل')),
                ('city', models.CharField(max_length=100, verbose_name='استان')),
                ('how_startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.startup', verbose_name='انتخاب استارتاب')),
            ],
            options={
                'verbose_name': 'ثبت نام در استارتاپ',
                'verbose_name_plural': 'ثبت نام در استارتاپ ها',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='CourseRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('family', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('father_name', models.CharField(max_length=100, verbose_name='نام پدر')),
                ('meli_code', models.BigIntegerField(verbose_name='کدملی')),
                ('birthday', models.CharField(max_length=10, verbose_name='تاریخ تولد')),
                ('status', models.CharField(choices=[('u', 'دانشجو'), ('g', 'فارغ التحصیل'), ('s', 'دانش آموز'), ('n', 'هیچکدام')], max_length=1, verbose_name='وضعیت تحصیلی')),
                ('reshte', models.CharField(max_length=150, verbose_name='رشته')),
                ('uni_name', models.CharField(max_length=200, verbose_name='نام محل تحصیل')),
                ('phone', models.CharField(max_length=15, verbose_name='تلفن')),
                ('email', models.EmailField(max_length=150, verbose_name='ایمیل')),
                ('city', models.CharField(max_length=100, verbose_name='استان')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.courses', verbose_name='انتخاب دوره')),
            ],
            options={
                'verbose_name': 'ثبت نام دوره آموزشی',
                'verbose_name_plural': 'ثبت نام دوره های آموزشی',
                'ordering': ('-name',),
            },
        ),
    ]
