from django.shortcuts import render

def nature_info(request):
    return render(request,'testapp/index.html')


def flower_info(request):
    head_msg='Flower facts'
    msg1="Flowers are the natural beauty"
    msg2="uses for decorations"
    msg3="beauty of plants"
    type='flower'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type}
    return render(request,'testapp/info.html',my_dict)

def water_info(request):
    head_msg='Water facts'
    msg1="Be clam like deep water"
    msg2="uses for daily purpose"
    msg3="NO water no life"
    type='water'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type}
    return render(request,'testapp/info.html',my_dict)

def temple_info(request):
    head_msg='Temple facts'
    msg1="temples are the historical places"
    msg2="positive vibes"
    msg3="worship of hindus"
    type='temple'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type}
    return render(request,'testapp/info.html',my_dict)        
