from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 🛠️ لوحة التحكم الإدارية
    path('admin/', admin.site.urls),

    # 🏠 الصفحة الرئيسية (home) — من تطبيق المنتجات
    path('', include('products.urls')),  # هذا هو المسار الرئيسي للموقع

    # 👤 حسابات المستخدمين (تسجيل، دخول، ملف شخصي)
    path('accounts/', include('accounts.urls')),

    # 📦 الطلبات وإدارة المشتريات
    path('orders/', include('orders.urls')),
]


# =============================
# 🖼️ إعداد عرض ملفات الوسائط (Media) أثناء التطوير
# =============================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 🎨 إعداد عرض الملفات الثابتة (Static) أثناء التطوير

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    path('accounts/', include('accounts.urls')),

