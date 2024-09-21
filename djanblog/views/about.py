from django.shortcuts import render

def about(request):
    """
    Returns a rendered html page about the blog.

    :param request: an HttpRequest object
    :return: an HttpResponse object
    """
    return render(request, 'about.html', {})
