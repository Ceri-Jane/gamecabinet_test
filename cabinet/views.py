from django.shortcuts import render

def my_cabinet(request):
    return render(request, 'cabinet/my_cabinet.html')