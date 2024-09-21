from django.shortcuts import render
from ..models.post import Post

def home(request):
    """
    Returns a rendered html page with 10 posts.

    :param request: an HttpRequest object
    :return: an HttpResponse object
    """
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})
