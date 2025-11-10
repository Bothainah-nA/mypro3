from django.urls import path
from . import views

urlpatterns = [
    # الصفحة الرئيسية للعملاء
    path('', views.home, name='home'),
]
