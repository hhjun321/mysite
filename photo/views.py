# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Photo
from photo.forms import PhotoEditForm
from photo.method import shutdown, pingChk, openCam
# Create your views here.

def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    print(photo.image_file.url)
    response_text = '<p>{photo_id}번 ... {photo_id}번 사진출력</p>'
    response_text += '<p>{photo_url}</p>'
    response_text += '<p><img src="{photo_url}" width=200 height=200/></p>'
    return HttpResponse(response_text.format(
                                            photo_id=photo_id,
                                            photo_url=photo.image_file.url))
    
def new_photo(request):
    if request.method == "GET":        
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)
        '''
        if edit_form.is_valid():
            new_photo = edit_form.save()
            
            return redirect(new_photo.get_absolute_url())
        '''
    
    return render(request, 'new_photo.html', {
                                                'form':edit_form,})
    
def index(request):
    response_text = ""
    latest_photo_list = Photo.objects.order_by('-created_at')[:5]
    if latest_photo_list.count()>0:        
        for photo in latest_photo_list:  
            response_text += '<p><img src="' + photo.image_file.url + '" width=200 height=200/></p>'   
        print(response_text)    
        
    chk = "N"
    ip = '172.30.1.45'
    res = pingChk(ip)
    if res==0:
        print('up')
        chk = "Y"
    else:
        print('down')        
    
    
    context = {'latest_photo_list': latest_photo_list,
               'response_text': response_text,
               'chk':chk,}
    return render(request, 'photo/index.html', context)


def out(request):
    print("enter")
    ip = '172.30.1.45'
    res = pingChk(ip)
    if res==0:
        print('up')
        shutdown(ip)
    else:
        print('down')        
        
        
    return index(request)
    
#test
def open(request):
    print("cam enter")
    openCam()
    return HttpResponseRedirect(reverse('photo:index'))
    