from django.shortcuts import render
from news.models import News
from service.models import Service
def home(request):
    data=News.objects.all()

    return render(request,'index.html',{'newsset':data})

def about(request):
    data=News.objects.all()

    return render(request,'about.html',{'dataset':data})

def service(request):
    try:
        if request.method=="GET":
            st=request.GET['search'];
            if st!=None:
                data=Service.objects.all().filter(service_title__icontains=st)
            else:
                data=service.objects.all()
    except:
        data=service.objects.all()
    return render(request,'service.html',{'dataset':data})

def price(request):
    return render(request,'price.html')

def new_details(request,nid):
    data=News.objects.get(id=nid)
    return render(request,'news-details.html',{'data':data})

def service_details(request,nid):
    data=Service.objects.get(id=nid)
    return render(request,'service-detail.html',{'data':data})


def contact(request):
    return render(request,'contact.html')

def app1(request):
    try:
        a=int(request.GET['t1']);
        b=int(request.GET['t2']);
        c=a+b
        #print("Sum is ",c)
        data={
            'a':a,
            'b':b,
            'c':c
        }
    except:
        pass
    return render(request,'app1.html',data)

def app2(request):
    try:
        a=int(request.GET['a1']);
        b=int(request.GET['a2']);
        c=int(request.GET['a3']);
        d=(a*b*c)/100
        data={
            'a':a,
            'b':b,
            'c':c,
            'd':d
        }
    except:
        pass
    return render(request,'app2.html',data)
