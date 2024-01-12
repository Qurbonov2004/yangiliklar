from datetime import datetime
from django.shortcuts import render

def main(request):
    return render(request,'admin/index.html')


def yangilik(request):
    context={
        "vaqt":datetime.now()

    }
    return render(request,'yangi/index.html',context)

def contact(request):
    return render(request,'yangi/contact.html')

def categori(request):
    return render(request,'yangi/categori.html')

def lates_news(request):
    return render(request,'yangi/latest_news.html')



