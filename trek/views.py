from django.shortcuts import render,redirect
from .models import Product,upi
from .forms import Formm,Formm1
from .mail import maiil
from django.http import HttpResponse
import datetime



from django.shortcuts import render

from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import render_to_pdf
from django.views.generic import View


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        sales = upi.objects.last()
        x = datetime.datetime.now()

        upiname = sales.upiname
        email = sales.email
        transid = sales.transid
        params={'upiname': upiname, 'email': email, 'transid': transid,'datetime':x}
        pdf = render_to_pdf('trek/pdf.html',params)

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')







def index(request):
    return render(request,'trek/index.html',{})
def package(request):
    return render(request,'trek/packages.html',{})
def pack1(request):
    return render(request,'trek/single-blog.html',{})
def pack2(request):
    return render(request,'trek/chopta.html',{})
def pack3(request):
    return render(request,'trek/devkyara.html',{})
def pack4(request):
    return render(request,'trek/harkidoon.html',{})
def pack5(request):
    return render(request,'trek/pras.html',{})
def pricc(request):

    data= Product.objects.last()
    if data.couponcode== 'nit'  and data.trek=='Har Ki Doon':
        a='2000'
        data.price=a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a,'form':form})
    elif data.couponcode is not 'nit' and data.trek =='kedarkantha':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode== 'nit'  and data.trek=='kedarkantha' :
        a='29000'
        data.price=a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode is not 'nit' and data.trek == 'Har Ki Doon':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode== 'nit' and data.trek == 'chopta/tungnath/deoriya tal':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode is not 'nit' and data.trek == 'Devkyara':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode== 'nit' and data.trek == 'Devkyara':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode is not 'nit' and data.trek == 'chopta/tungnath/deoriya tal':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode == 'nit' and data.trek == 'Parashar Lake,Mandi':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode is not 'nit' and data.trek == 'Parashar Lake,Mandi':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode == 'nit' and data.trek == 'Karthik Swami':
        a = '29000'
        data.price = a
        data.save()
        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})
    elif data.couponcode is not 'nit' and data.trek == 'Karthik Swami':
        a = '29000'
        data.price = a
        data.save()

        form = Formm1
        if request.method == 'POST':
            form = Formm1(request.POST)
            if form.is_valid():
                form.save()
                list = upi.objects.last()

                maiil(
                    "new request for " + list.upiname + "with transaction id =" + list.transid + " open admin... to confirm the booking")
                return redirect('/render/pdf')
            else:
                form = Formm1()
        return render(request, 'trek/final.html', {'a': a, 'form': form})




def bookk(request):

    form = Formm()

    if request.method == 'POST':
        a=request.POST.get('name')
        form = Formm(request.POST,request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            trek = form.cleaned_data['trek']
            coupon=form.cleaned_data['couponcode']
            height=form.cleaned_data['height']
            weight=form.cleaned_data['weight']
            id_proof=form.cleaned_data['id_proof']


            p=Product(name=name,address=address,trek=trek,couponcode=coupon,confirm='no',height=height,weight=weight,id_proof=id_proof)
            p.save()


            #form.save()

            return redirect('/final')

        else:
            form = Formm()

    return render(request, 'trek/contact.html', {'form': form})



