from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team
# Create your views here.
def demo(request):
    # return HttpResponse("Hello World")
    obj=Place.objects.all()
    objct=Team.objects.all()
    return render(request,'index.html',{'result':obj,'res':objct})
# def about(rquest):
#     return render(rquest,'about.html')
# def contact(request):
#     return HttpResponse("this is to test contact")