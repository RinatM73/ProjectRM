from django.shortcuts import render
import datetime
# Create your views here.
def prog_day(request):
    year = datetime.date.today().year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        prog_day = (f'12-09-{year}')
    else:
        prog_day = (f'13-09-{year}')
    return render(request, 'prog_day/prog_day.html', {'prog_day' : prog_day})