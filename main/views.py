from django.shortcuts import render
from main.models import Main, MainBanner
from django.http import Http404
from django.shortcuts import get_object_or_404
from gc import get_objects
import time


from main.method import shutdown, pingChk
from main.TTS_대기정보 import get_text,convert_textTomp3,play_mp3
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
    
    
    text = get_text()
    convert_textTomp3(text)
    play_mp3()
    return HttpResponseRedirect(reverse('photo:index'))