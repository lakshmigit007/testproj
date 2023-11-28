from django.shortcuts import render
from .models import StudentData

# Create your views here.
def displayform(request):
    if request.method=='GET':
       return render(request,'studentform.html')
    else:
        StudentData(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            mob=request.POST.get('mob')
        ).save()
    stdform=StudentData.objects.all()
    return render(request,'studentform.html',{'stdform':stdform})