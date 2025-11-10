from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    """مدير مخصص لإنشاء المستخدمين والمشرفين"""

    def create_user(self, username, email=None, password=None, **extra_fields):
        """إنشاء مستخدم عادي"""
        if not username:
            raise ValueError(_("اسم المستخدم مطلوب"))
        if not email:
            raise ValueError(_("البريد الإلكتروني مطلوب"))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """إنشاء مستخدم مشرف (Superuser)"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("يجب أن يكون المشرف لديه is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("يجب أن يكون المشرف لديه is_superuser=True"))

        return self.create_user(username, email, password, **extra_fields)


class Account(AbstractUser):
    """نموذج المستخدم المخصص"""
    email = models.EmailField(
        _("البريد الإلكتروني"),
        unique=True,
        blank=False,
        null=False
    )
    phone = models.CharField(
        _("رقم الجوال"),
        max_length=20,
        blank=True,
        null=True
    )

    objects = AccountManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("حساب مستخدم")
        verbose_name_plural = _("حسابات المستخدمين")
