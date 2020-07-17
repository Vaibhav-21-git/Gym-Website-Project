from django.shortcuts import render
from .models import Gallery
from contact_us.models import Contact_Info
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from classes.models import Class
from pages.models import Banner
def index(request):
    banner = Banner.objects.filter(page="gallery").first()
    gallery = Gallery.objects.all()
    paginator = Paginator(gallery,9)    
    page = request.GET.get('page')
    paged_gallery = paginator.get_page(page)
    classes = Class.objects.all()
    display = paged_gallery
    
    buffet = len(classes) + 1
    gym = len(classes) + 2
       
    context = {
        "classes" : classes,
        'gym' : gym,
        'buffet' : buffet,
        'banner' : banner,
        'gallery' : display,
    }

    
    return render(request, './gallery.html',context)