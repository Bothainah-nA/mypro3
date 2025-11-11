from django.db import models
from django.utils.translation import gettext_lazy as _  # لدعم اللغة العربية في لوحة التحكم
from cloudinary.models import CloudinaryField  # ✅ استيراد حقل CloudinaryField لرفع الصور للسحابة


class Category(models.Model):
    """
    تصنيفات المنتجات (مثل: أواني الطبخ، أدوات المائدة، ديكور)
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("اسم التصنيف")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("الوصف")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")
        ordering = ["name"]


class Product(models.Model):
    """
    تفاصيل المنتج داخل المتجر
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("التصنيف")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("اسم المنتج")
    )
    description = models.TextField(
        verbose_name=_("الوصف")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر")
    )

    # ✅ الحقل الذي يرفع الصور تلقائيًا إلى Cloudinary
    image = CloudinaryField(
        "صورة المنتج",
        folder="products/",     # اسم المجلد داخل حسابك في Cloudinary
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_("الكمية المتوفرة")
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name=_("متوفر؟")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإضافة")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("آخر تحديث")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ["-created_at"]
