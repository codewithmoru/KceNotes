from django.shortcuts import render, HttpResponse
#from .models import Contact
from datetime import datetime
from .models import Notes1
from .models import Notes2
from .models import Notes3
from .models import Notes4
from .models import TEACHING
from math import ceil
from django.contrib import messages
from .forms import CustomerForm

# Create your views here.

def home(request):
    return render(request, "index.html")

def notes1(request):
    products= Notes1.objects.all()
    allProds=[]
    catprods= Notes1.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Notes1.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"notes1.html", params)


def notes2(request):
    products= Notes2.objects.all()
    allProds=[]
    catprods= Notes2.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Notes2.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"notes2.html", params)

def notes3(request):
    products= Notes3.objects.all()
    allProds=[]
    catprods= Notes3.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Notes3.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"notes3.html", params)

def notes4(request):
    products= Notes4.objects.all()
    allProds=[]
    catprods= Notes4.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Notes4.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"notes4.html", params)    

def about(request):
    return render(request, "about.html")    


def teaching(request):

    products= TEACHING.objects.all()
    allProds=[]
    catprods= TEACHING.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=TEACHING.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"Examkida.html", params)


# Create your views here.

def cndex(request):

	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():

			form.save()
			
	context = {'form':form}
	return render(request, 'contact.html', context)


def Register(request):

  form = CustomerForm()
  
  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
        
       form.save()
       
  context = {'form':form}
  return render(request, 'register.html', context)    
    