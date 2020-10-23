from django.shortcuts import render

# Create your views here.

from django.core.files.storage import FileSystemStorage
from app.forms import *

def image_form(request):
    form=ImageForm()
    if request.method=='POST' and request.FILES:
        form_data=ImageForm(request.POST,request.FILES)
        if form_data.is_valid():
            img=form_data.cleaned_data['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            image_url=fs.url(file)
            return render(request,'image_display.html',context={'image_url':image_url})

    return render(request,'form.html',context={'form':form})


