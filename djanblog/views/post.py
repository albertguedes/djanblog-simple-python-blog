from django.shortcuts import render
from ..models import Post

def post(request, id):
    """
    Returns a rendered html page with a post.

    :param request: an HttpRequest object
    :return: an HttpResponse object
    """
    post = Post.objects.get(id=id)
    
    return render(request, 'post.html', {'post': post})
