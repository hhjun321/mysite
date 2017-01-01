from django.shortcuts import render
from main.models import Main, MainBanner
from django.http import Http404
from django.shortcuts import get_object_or_404
from gc import get_objects
# Create your views here.
def index(request):
    main = Main.objects
    main_id = unicode(str(main.get().id))
    main_banner = MainBanner.objects.filter(main_id = main_id)
    #template = loader.get_template('polis/index.html')
    print(main,main_banner)
    context = {'main': main.get(),
               'main_banner': main_banner}
    return render(request, 'main/index.html', context)
