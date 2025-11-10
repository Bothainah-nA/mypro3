from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _  # لدعم اللغة العربية في لوحة التحكم

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = _('إدارة الحسابات')

