from django.shortcuts import render

def reg_user(request):
    return render(request, 'reg_user/reg_user.html')

def log_user(request):
    return render(request, 'log_user/log_user.html')