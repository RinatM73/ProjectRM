from django.shortcuts import render

def questView(request):
    return render(request, 'quest.html')
