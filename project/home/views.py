from django.shortcuts import render
from meals.models import Meal,Categorie
from blog.models import Post
from aboutus.models import WhyChooseUs
# Create your views here.
def home(request):

    meals = Meal.objects.all()
    categories = Categorie.objects.all()
    posts = Post.objects.all()
    last_post = Post.objects.last()
    aboutus = WhyChooseUs.objects.all()
    context={
    'meals':meals,
    'categories':categories,
    'posts':posts,
    'last_post':last_post,
    'aboutus':aboutus
    }


    return render(request,'home/index.html',context)
