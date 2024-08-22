from django.shortcuts import render
from .models import BlogModel       # we added
from django.shortcuts import get_object_or_404  # we added

# Create your views here.


def blog_allUrls(request):

    blog = BlogModel.objects.all()
    # blog = BlogModel.objects.order_by('-id')[:2]  # Retrieves 5 most recent objects based on their IDs

    return render(request, "blog/blog_allUrls/blog.html", {"blogs": blog})


def detail(request, blog_id):
    
    blog = get_object_or_404(BlogModel, pk=blog_id)     # get_object_or_404() is a method which check if our BlogModel site is available or not; pk(primary key) In Django models, each model has a primary key field that uniquely identifies each record in the database table.
    
    return render(request, 'blog/blog_allUrls/detail.html', {'id':blog_id, 'blog':blog})
