from django.shortcuts import render

# Create your views here.
def shelem_main(request):
    return render(request,'reg.html')