from django.shortcuts import render

# Create your views here.

def port_list(request):
    return render(request, 'blog/post_list.html', {})
