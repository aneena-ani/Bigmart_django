from django.shortcuts import render,redirect
from backend.models import catedb,prodb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index_page(req):
    return render(req,"index.html")
def category(req):
    return render(req,"category.html")
def save_cate(req):
    if req.method=="POST":
        na = req.POST.get('name')
        img = req.FILES['image']
        des = req.POST.get('description')
        obj = catedb(name=na,image=img,description=des)
        obj.save()
        messages.success(req,"category saved succesfully")
        return redirect(category)
def display_cate(req):
    data = catedb.objects.all()
    return render(req,"display.html",{'data':data})
def edit_cate(req,cateid):
    data = catedb.objects.get(id=cateid)
    return render(req,"edit.html",{'data':data})
def update_cate(request,cateid):
    if request.method=="POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catedb.objects.get(id=cateid).image
        catedb.objects.filter(id=cateid).update(name=na,description=des,image=file)
        messages.success(request, "successfully updated")
        return redirect(display_cate)


def delete_cate(req,cateid):
    d = catedb.objects.filter(id=cateid)
    d.delete()
    messages.error(req, " succesfully deleted")
    return redirect(display_cate)
def admin_page(req):
    return render(req,"adminlogin.html")

def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "welcome")
                return redirect(index_page)
            else:
                messages.error(request, "invalid password")
                return redirect(admin_page)
        else:
            messages.warning(request, "user not found")
            return redirect(admin_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(admin_page)

def product_page(request):
    cat = catedb.objects.all()
    return render(request,"products.html",{'cat':cat})

def save_product(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pna = request.POST.get('pname')
        des = request.POST.get('description')
        img = request.FILES['pimage']
        pr = request.POST.get('price')
        obj = prodb(catname=na,proname=pna, description=des, pimage=img,price=pr)
        obj.save()
        messages.success(request, "product saved successfully")
        return redirect(product_page)

def display_products(request):
    data = prodb.objects.all()
    return render(request,"displaypro.html",{'data':data})
def edit_products(request,proid):
    cat=catedb.objects.all()
    data = prodb.objects.get(id=proid)
    return render(request,"editpro.html",{'data':data,'cat':cat})

def update_pro(request,proid):
    if request.method=="POST":
        na = request.POST.get('name')
        pna = request.POST.get('pname')
        des = request.POST.get('description')
        try:
            img = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = prodb.objects.get(id=proid).pimage
        pr = request.POST.get('price')
        prodb.objects.filter(id=proid).update(catname=na,proname=pna, description=des, pimage=file,price=pr)
        messages.success(request, "successfully updated")
        return redirect(display_products)

def delete_pro(request,proid):
    d = prodb.objects.filter(id=proid)
    d.delete()
    messages.error(request, "successfully deleted")
    return redirect(display_products)