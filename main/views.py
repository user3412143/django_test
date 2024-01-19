from django.shortcuts import render

def default_page(request):
     return render(request, 'index.html') 
