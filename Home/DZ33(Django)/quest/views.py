from django.shortcuts import render

def quest(request):
    return render(request, 'quest/quest.html')
