from django.shortcuts import render
from django.shortcuts import redirect  #добавленное

def encyclopedia_view(request):
    return render(request, 'myapp/encyclopedia.html')
def page2_view(request):
    return render(request, 'myapp/page2.html')