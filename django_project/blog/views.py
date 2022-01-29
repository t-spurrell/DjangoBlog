from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Trevor',
        'title': 'blog Post 1',
        'content': 'First post content',
        'date': 'July 18, 2021'
    },
    {
        'author': 'Tom',
        'title': 'blog Post 2',
        'content': 'Second post content',
        'date': 'July 19, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')


