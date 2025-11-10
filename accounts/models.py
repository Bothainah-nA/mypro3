from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _  # لدعم اللغة العربية في لوحة التحكم

class Account(AbstractUser):
    """
    نموذج مخصص للمستخدمين (يستبدل User الافتراضي في Django)
    """
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_("رقم الجوال")
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("العنوان")
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("المدينة")
    )
    is_customer = models.BooleanField(
        default=True,
        verbose_name=_("هل هو عميل؟")
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name=_("هل هو مدير؟")
    )

    def __str__(self):
        # عرض الاسم بشكل واضح في لوحة التحكم
        return f"{self.username} - {self.get_full_name() or 'بدون اسم كامل'}"

    class Meta:
        verbose_name = _("حساب المستخدم")
        verbose_name_plural = _("حسابات المستخدمين")
        ordering = ["username"]
