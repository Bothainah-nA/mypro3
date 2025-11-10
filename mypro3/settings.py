from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# =============================
# 📂 المسارات الأساسية
# =============================
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / 'templates'   # مجلد القوالب العام
STATIC_DIR = BASE_DIR / 'static'         # مجلد الملفات الثابتة أثناء التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'   # مجلد تجميع الملفات الثابتة عند التنفيذ
MEDIA_DIR = BASE_DIR / 'media'           # مجلد ملفات الوسائط (المرفوعة من المستخدمين)


# =============================
# 🔐 مفتاح الأمان (يُستخدم فقط في بيئة التطوير)
# =============================
SECRET_KEY = 'django-insecure-!b95e8l4s7egpsuiq9c7__tgtexuxophsf#t(d4k(jti80d=-g'


# =============================
# ⚙️ وضع التطوير
# =============================
DEBUG = True
ALLOWED_HOSTS = []


# =============================
# 🧩 التطبيقات المثبتة Installed Apps
# =============================
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts',
    'products',
    'orders',

    # مكتبة Cloudinary لتخزين الوسائط
    'cloudinary',
    'cloudinary_storage',
]


# =============================
# ⚙️ الوسائط Middleware
# =============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =============================
# 🌐 إعدادات الروابط والقوالب Templates
# =============================
ROOT_URLCONF = 'mypro3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # المسار العام للقوالب
        'DIRS': [TEMPLATES_DIR],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =============================
# 🚀 إعدادات التطبيق الرئيسي
# =============================
WSGI_APPLICATION = 'mypro3.wsgi.application'


# =============================
# 🗄️ قاعدة البيانات
# =============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================
# 🔐 التحقق من كلمات المرور
# =============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =============================
# 🌍 اللغة والمنطقة الزمنية
# =============================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True


# =============================
# 🎨 الملفات الثابتة (Static Files)
# =============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # المسار النهائي لتجميع الملفات


# =============================
# 🖼️ ملفات الوسائط (Media Files)
# =============================
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR


# =============================
# ☁️ إعدادات Cloudinary لتخزين الوسائط
# =============================
cloudinary.config(
    cloud_name='dnblq6aft',             # ✅ الاسم الصحيح من حسابك Cloudinary
    api_key='184872396444896',          # ✅ مفتاح API من حسابك
    api_secret='QP3aA8ObVr_OvHs66ES3QBfFCHk'  # ✅ المفتاح السري من حسابك
)

# جعل Django يستخدم Cloudinary كمخزن وسائط افتراضي
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# =============================
# 🧱 الإعداد الافتراضي لمعرف الجداول
# =============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =============================
# 👥 تفعيل نموذج المستخدم المخصص
# =============================
AUTH_USER_MODEL = 'accounts.Account'
