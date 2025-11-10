from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

@admin.register(Account)
class AccountAdmin(UserAdmin):
    """إدارة المستخدمين (الحسابات) في لوحة التحكم"""
    list_display = ('username', 'email', 'phone', 'city', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_admin', 'is_customer')
    search_fields = ('username', 'email', 'phone', 'city')
    ordering = ('username',)

    # الحقول التي تظهر في صفحة التفاصيل داخل لوحة الإدارة
    fieldsets = (
        ('المعلومات الأساسية', {'fields': ('username', 'email', 'password')}),
        ('البيانات الشخصية', {'fields': ('first_name', 'last_name', 'phone', 'address', 'city')}),
        ('الأذونات', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_customer', 'groups', 'user_permissions')}),
        ('تواريخ مهمة', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('بيانات إنشاء الحساب', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_customer', 'is_admin'),
        }),
    )
