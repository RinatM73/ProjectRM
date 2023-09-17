from django.shortcuts import render

# Create your views here.
def multip_table(request):
    list = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'multip_table/multip_table.html', context={'list' : list})
