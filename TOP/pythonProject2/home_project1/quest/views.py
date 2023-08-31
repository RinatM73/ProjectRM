from django.shortcuts import render

def questView(request):
    my_name = request.GET.get('quest/quest.html')
    return render(request, template_name='quest/quest.html')
