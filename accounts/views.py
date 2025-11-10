from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import AccountCreationForm, AccountLoginForm


def register_view(request):
    """إنشاء حساب جديد"""
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "🎉 تم إنشاء الحساب بنجاح! مرحبًا بك في كنزا 🛍️")
            return redirect('home')
        else:
            messages.error(request, "⚠️ الرجاء تصحيح الأخطاء أدناه.")
    else:
        form = AccountCreationForm()

    return render(request, 'accounts-templates/register.html', {'form': form})


def login_view(request):
    """تسجيل الدخول"""
    if request.method == 'POST':
        form = AccountLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"✅ أهلاً {user.username}، تم تسجيل الدخول بنجاح!")
            return redirect('home')
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
    else:
        form = AccountLoginForm()

    return render(request, 'accounts-templates/login.html', {'form': form})


def logout_view(request):
    """تسجيل الخروج"""
    logout(request)
    messages.info(request, "👋 تم تسجيل الخروج بنجاح، نراك قريبًا!")
    return redirect('home')
