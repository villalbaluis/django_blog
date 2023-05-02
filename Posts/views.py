from django.shortcuts import render

def home(request):
    return render(request, 'Posts/posts_page.html')