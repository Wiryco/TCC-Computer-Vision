from django.shortcuts import render

def homepage_view(request):
    return render(request, 'core/homepage.html', {})

def index_view(request):
    return render(request, 'core/description.html')

def teste_web_cam(request):
    return render(request, 'facerec_from_webcam_faster.py', {})

# def base_pyview(request):
#     return render(request, 'core/index.html')
