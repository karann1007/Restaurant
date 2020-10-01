from django.shortcuts import render
from .models import AboutUs,Chef,WhyChooseUs
# Create your views here.
def aboutus_list(request):
    about = AboutUs.objects.last()
    whychooseus= WhyChooseUs.objects.all()
    chef= Chef.objects.all()

    context = {
        'about': about,
        'whychooseus' : whychooseus,
        'chef':chef
    }

    return render(request,'aboutus/aboutus.html',context)
