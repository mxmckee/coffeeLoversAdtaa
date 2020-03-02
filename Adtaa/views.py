from django.shortcuts import render


#this is the views page for the adtaa

def index(request):
    return render(request, 'Adtaa/index.html')
