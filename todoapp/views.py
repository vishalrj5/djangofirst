from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import Tasks
# Create your views here.
# task create html,view
def create_task(request):
    return render(request,"mytodoapp/createtask.html")

def addTask(request):
    my_task=request.POST.get("task")
    date=request.POST.get("date")
    status=request.POST.get("status")
    task=Tasks(task_name=my_task,date=date,status=status)
    task.save()
    print(my_task,date,status)
    print("savedddd")
    context={
    }
    tasks=Tasks.objects.all()
    context["task"]=tasks
    # context[""]
    return render(request,"mytodoapp/createtask.html",context)

def calc(request):
    return render(request,"mytodoapp/calc.html")

def ad(request):
    n1=int(request.POST.get("num1"))
    n2=int(request.POST.get("num2"))
    sum=n1+n2
    context={

    }
    context["sum"]=sum
    return render(request,"mytodoapp/calc.html",context)

def sub(request):
    n1=int(request.POST.get("num1"))
    n2=int(request.POST.get("num2"))
    sub=n1-n2
    context={

    }
    context["sub"]=sub
    return render(request,"mytodoapp/calc.html",context)

def mul(request):
    n1=int(request.POST.get("num1"))
    n2=int(request.POST.get("num2"))
    mul=n1*n2
    context={

    }
    context["mul"]=mul
    return render(request,"mytodoapp/calc.html",context)



