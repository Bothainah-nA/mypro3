from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية من تطبيق المنتجات
    path('', include('products.urls')),

    # تطبيق الحسابات (تسجيل الدخول/إنشاء حساب)
    path('accounts/', include('accounts.urls')),

    # تطبيق الطلبات (إن وجد)
    path('orders/', include('orders.urls')),
]

# إعداد عرض الصور في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
