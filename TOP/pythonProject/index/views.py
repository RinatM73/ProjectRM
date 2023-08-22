from django.shortcuts import render
import random

# Create your views here.
def indexViews(request):
    return render(request, 'index.html')

def passwordView(request):
    newpassword = ''
    length = int(request.GET.get('length'))
    text = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        text.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        text.extend('1234567890')
    if request.GET.get('symbols'):
        text.extend('!@#$%^&*()_+=-')
    for i in range(length):
        newpassword += text[random.randint(0,len(text)-1)]


                         #                                        из HTML       из Python
    return render(request, 'password.html', {'newpassword':newpassword})