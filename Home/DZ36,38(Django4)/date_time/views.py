from django.shortcuts import render

# Create your views here.
def date_time(request):
    return render(request, 'date_time/date_time.html')

