from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from products.models import Product


class Order(models.Model):
    """
    الطلب الذي يقوم به المستخدم
    """

    class Status(models.TextChoices):
        PENDING = 'pending', _('قيد المعالجة')
        SHIPPED = 'shipped', _('تم الشحن')
        DELIVERED = 'delivered', _('تم التوصيل')
        CANCELLED = 'cancelled', _('ملغي')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("المستخدم")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ الإنشاء")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("آخر تحديث")
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_("الحالة")
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name=_("إجمالي السعر")
    )

    def __str__(self):
        return f"طلب رقم {self.id} للمستخدم {self.user.username}"

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
        ordering = ["-created_at"]


class OrderItem(models.Model):
    """
    عناصر الطلب (المنتجات داخل الطلب الواحد)
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("الطلب")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("المنتج")
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_("الكمية")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("السعر عند الشراء")
    )

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    class Meta:
        verbose_name = _("عنصر طلب")
        verbose_name_plural = _("عناصر الطلب")
        ordering = ["order"]
