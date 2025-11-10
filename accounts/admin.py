from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    """إدارة المستخدمين (الحسابات) في لوحة التحكم"""

    # الأعمدة التي تظهر في قائمة المستخدمين داخل لوحة التحكم
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)

    # الحقول التي تظهر عند عرض تفاصيل المستخدم داخل لوحة الإدارة
    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('username', 'email', 'password')
        }),
        ('البيانات الشخصية', {
            'fields': ('first_name', 'last_name', 'phone')
        }),
        ('الأذونات والصلاحيات', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('تواريخ مهمة', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # الحقول التي تظهر عند إنشاء مستخدم جديد
    add_fieldsets = (
        ('بيانات إنشاء الحساب', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
