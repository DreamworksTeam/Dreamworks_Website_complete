from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'website/home.html', {})


def aboutpage(request):
    return render(request, 'website/about.html', {})


def web_design(request):
    return render(request, 'website/web-design.html', {})

def consulting(request):
    return render(request, 'website/consulting.html', {})
    
def graphic_design(request):
    return render(request, 'website/graphic-design.html', {})


def media_publishing(request):
    return render(request, 'website/media-publishing.html', {})


def social_entrepreneurship(request):
    return render(request, 'website/social-entrepreneurship.html', {})


def system_solution(request):
    return render(request, 'website/system-solution.html', {})


