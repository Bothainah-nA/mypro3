from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


class AccountCreationForm(UserCreationForm):
    """نموذج إنشاء حساب جديد للمستخدم المخصص Account"""

    email = forms.EmailField(
        label="البريد الإلكتروني",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل بريدك الإلكتروني'
        })
    )

    username = forms.CharField(
        label="اسم المستخدم",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل اسم المستخدم'
        })
    )

    password1 = forms.CharField(
        label="كلمة المرور",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل كلمة المرور'
        })
    )

    password2 = forms.CharField(
        label="تأكيد كلمة المرور",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أعد إدخال كلمة المرور'
        })
    )

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']


class AccountLoginForm(AuthenticationForm):
    """نموذج تسجيل الدخول"""
    username = forms.CharField(
        label="اسم المستخدم",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل اسم المستخدم'
        })
    )

    password = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل كلمة المرور'
        })
    )
