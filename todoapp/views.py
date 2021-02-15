from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# task create html,view
def create_task(request):
    return render(request,"mytodoapp/createtask.html")

def addTask(request):
    my_task=request.POST.get("task")
    print(my_task)
    context={
    }
    context["task"]=my_task
    return render(request,"mytodoapp/addd.html",context)

