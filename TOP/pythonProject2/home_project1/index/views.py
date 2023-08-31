from django.shortcuts import render

def indexView(request):
    return render(request, template_name='index/index.html')
