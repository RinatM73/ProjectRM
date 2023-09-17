from django.shortcuts import render

def quest(request):
    image_1 = request.GET.get('image_1')
    my_name = request.GET.get('my_name')
    my_secname = request.GET.get('my_secname')
    my_birthday = request.GET.get('my_birthday')
    my_skills1 = request.GET.get('my_skills1')
    my_skills2 = request.GET.get('my_skills2')
    my_skills3 = request.GET.get('my_skills3')
    my_skills4 = request.GET.get('my_skills4')
    my_skills5 = request.GET.get('my_skills5')
    about_me = request.GET.get('about_me')

    datas = {'image_1':image_1,
            'my_name':my_name,
            'my_secname':my_secname,
            'my_birthday':my_birthday,
            'my_skills1':my_skills1,
            'my_skills2':my_skills2,
            'my_skills3':my_skills3,
            'my_skills4':my_skills4,
            'my_skills5':my_skills5,
            'about_me':about_me}
    return render(request, 'quest/quest.html', context=datas)
