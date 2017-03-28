from django.shortcuts import render
from main.models import Main, MainBanner
from django.http import Http404
from django.shortcuts import get_object_or_404
from gc import get_objects
import time
import os


from main.method import shutdown, pingChk
# Create your views here.
def index(request):
    main = Main.objects
    main_id = unicode(str(main.get().id))
    main_banner = MainBanner.objects.filter(main_id = main_id)
    #template = loader.get_template('polis/index.html')
    print(main,main_banner)
    
    chk = "N"
    ip = '172.30.1.45'
    res = pingChk(ip)
    if res==0:
        print('up')
        chk = "Y"
    else:
        print('down')      
        
        
    context = {'main': main.get(),
               'main_banner': main_banner,
               'chk':chk,}
    return render(request, 'main/index.html', context)



def out(request):
    print("enter")
    ip = '172.30.1.45'
    res = pingChk(ip)
    
    if res==0:
        print('up')
        shutdown(ip)
        time.sleep(5)
    else:
        print('down')        
        
        
    return HttpResponseRedirect(reverse('photo:index'))

def weather(request):
    
    
    os.system('python3 /home/pi/python_test/센서_대기/TOUCH_바로실행.py')
    return HttpResponseRedirect(reverse('photo:index'))