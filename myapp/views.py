from django.shortcuts import render

def encyclopedia_view(request):
    return render(request, 'myapp/encyclopedia.html')
