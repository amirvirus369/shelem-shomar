from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from .models import CustomUser
import re

# ========================================================
# ۱. فرم اختصاصی برای ساخت کاربر جدید در پنل ادمین (Creation)
# ========================================================
class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='رمز عبور', 
        widget=forms.PasswordInput(attrs={'class': 'vTextField'}),
        help_text='یک رمز عبور قوی حداقل ۸ کاراکتری وارد کنید.'
    )
    confirm_password = forms.CharField(
        label='تایید رمز عبور', 
        widget=forms.PasswordInput(attrs={'class': 'vTextField'}),
        help_text='رمز عبور را مجدداً وارد کنید.'
    )

    class Meta:
        model = CustomUser
        fields = ('phone_number', 'full_name', 'avatar', 'is_premium')

    # اعتبارسنجی شماره تلفن در ادمین
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number = "".join(phone_number.split()) # حذف فضاهای خالی
        if not re.match(r'^09\d{9}$', phone_number):
            raise ValidationError('فرمت شماره تلفن معتبر نیست! باید با 09 شروع شده و ۱۱ رقم باشد.')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('این شماره تلفن قبلاً در سیستم ثبت شده است.')
        return phone_number

    # اعتبارسنجی یکسان بودن پسوردها در ادمین
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("🚨 رمز عبور و تاییدیه آن کاملاً با هم مغایرت دارند!")
            if len(password) < 8:
                raise ValidationError("🚨 رمز عبور باید حداقل ۸ کاراکتر باشد.")
        return cleaned_data

    # ذخیره امن پسورد (پسورد نباید به صورت متن ساده در دیتابیس ذخیره شود)
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# ========================================================
# ۲. فرم اختصاصی برای ویرایش کاربر موجود در پنل ادمین (Change)
# ========================================================
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'full_name', 'avatar', 'is_premium', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number = "".join(phone_number.split())
        if not re.match(r'^09\d{9}$', phone_number):
            raise ValidationError('فرمت شماره تلفن معتبر نیست!')
        
        # بررسی تکراری نبودن شماره با در نظر گرفتن اکانت فعلی
        if CustomUser.objects.filter(phone_number=phone_number).exclude(pk=self.instance.pk).exists():
            raise ValidationError('این شماره تلفن توسط کاربر دیگری رزرو شده است.')
        return phone_number

# ========================================================
# ۳. تنظیمات مدیریت پنل ادمین و فعال‌سازی بخش پرمیشن‌ها
# ========================================================
class CustomUserAdmin(UserAdmin):
    # متصل کردن فرم‌های سفارشی به بخش ادمین
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    # فیلدهایی که در جدول اصلی ادمین نمایش داده می‌شوند
    list_display = ['phone_number', 'full_name', 'is_premium', 'is_staff', 'is_active']
    list_filter = ['is_premium', 'is_staff', 'is_active', 'groups']
    search_fields = ['phone_number', 'full_name']
    ordering = ['phone_number']

    # چیدمان فیلدها هنگام ویرایش کاربر (اینجا بخش Permissions را فعال کردیم)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('اطلاعات فردی بازیکن', {'fields': ('full_name', 'avatar', 'is_premium')}),
        ('سطوح دسترسی و پرمیشن‌ها', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'description': 'از این بخش می‌توانید کاربر را عضو یک گروه خاص کنید یا پرمیشن‌های اتمیک (مانند افزودن، تغییر یا حذف دست‌ها) را مستقیماً به تیک بزنید.'
        }),
        ('تاریخ‌های مهم', {'fields': ('last_login',)}),
    )

    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password', 'confirm_password', 'full_name', 'avatar', 'is_premium', 'is_active', 'is_staff'),
        }),
    )

# ثبت نهایی در ادمین جنگو
admin.site.register(CustomUser, CustomUserAdmin)