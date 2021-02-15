from django.shortcuts import render

# Create your views here.
def login(request):
    print("Hello")
    return render(request,"myusers/login.html")