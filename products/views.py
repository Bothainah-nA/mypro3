from django.shortcuts import render

def home(request):
    # يعرض الصفحة الرئيسية من مجلد templates/
    return render(request, 'home.html')
