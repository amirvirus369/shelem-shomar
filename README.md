# پروژه شماره شلم

این پروژه با فریمورک Django توسعه داده شده است.
خب چون اولین پورژه ای که میخام قرار بدم رو گیت زیاد روی احراز هویتش کار نکردم

## تکنولوژی‌های استفاده شده

- Python
- Django
- django-simple-captcha

## نصب پروژه

ابتدا وابستگی‌ها را نصب کنید:

```bash
pip install -r requirements.txt
```

سپس مایگریشن‌ها را اجرا کنید:

```bash
python manage.py makemigrations
python manage.py migrate
```

در نهایت سرور را اجرا کنید:

```bash
python manage.py runserver
```