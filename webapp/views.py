from django.shortcuts import render,redirect
from backend.models import prodb,catedb
from webapp.models import contactdb, registerdb,cartdb
from django.contrib import messages


# Create your views here.
def homepage(req):
    cat = catedb.objects.all()
    return render(req,"home.html",{'cat':cat})

def aboutpage(req):
    cat = catedb.objects.all()
    return render(req,"about.html",{'cat':cat})

def contactpage(req):
    cat = catedb.objects.all()
    return render(req,"contact.html",{'cat':cat})

def ourproducts(req):
    cat = catedb.objects.all()
    pro = prodb.objects.all()
    return render(req,"ourproducts.html",{'products':pro,'cat':cat})

def savecontact(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        ph = req.POST.get('phone')
        sub = req.POST.get('subject')
        msg = req.POST.get('message')
        obj=contactdb(cname=na,cemail=em,cphone=ph,csubject=sub,cmessage=msg)
        obj.save()
        return redirect(contactpage)
def contactdata(req):
    data = contactdb.objects.all()
    return render(req,"contactdata.html",{'data':data})

def deletedata(req,conid):
    x = contactdb.objects.filter(id=conid)
    x.delete()
    return redirect(contactdata)
def pro_filtered(req,cat_name):
    data = prodb.objects.filter(catname=cat_name)
    return render(req,"products_filtered.html",{'data':data})

def singleproduct(req,proid):
    cat = catedb.objects.all()
    data = prodb.objects.get(id=proid)
    return render(req,"singleproduct.html",{'data':data,'cat':cat})
def reg_page(req):
    return render(req,"register.html")

def save_reg(req):
    if req.method=="POST":
        us=req.POST.get("name")
        em=req.POST.get("email")
        pa=req.POST.get("pass1")
        pas=req.POST.get("pass2")
        obj=registerdb(Username=us,Email=em,Password=pa,Confirm_Password=pas)
        if registerdb.objects.filter(Username=us).exists():
            messages.warning(req,"username  already exists!")
            return redirect(reg_page)
        elif registerdb.objects.filter(Email=em).exists():
            messages.warning(req,"email already exists!")
            return redirect(reg_page)
        else:
            obj.save()
            messages.success(req,"successfully registered")
        return redirect(userlogin_page)


def userlogin(req):
    if req.method=="POST":
        us=req.POST.get("username")
        pas=req.POST.get("password")
        if registerdb.objects.filter(Username=us, Password=pas).exists():
            req.session['Username'] = us
            req.session['Password'] = pas
            messages.success(req,"Login sucessfully")
            return redirect(homepage)
        else:
            return redirect(reg_page)
    else:
        return redirect(reg_page)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request,"User logout successfully")
    return redirect(homepage)


def save_cart(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pr_name=request.POST.get('pname')
        quant = request.POST.get('quantity')
        tot = request.POST.get('total')
        obj=cartdb(Username=un,Productname=pr_name,Quantity=quant,Totalprice=tot)
        obj.save()
        messages.success(request, "Add to Cart Successfully")
        return redirect(homepage)

def cart_page(request):
    data=cartdb.objects.filter(Username=request.session['Username'])
    total=0
    for d in data:
        total= total+d.Totalprice
    return render(request,"cart.html" ,{'data':data, 'total':total})

def delete_item(request,p_id):
    x = cartdb.objects.filter(id=p_id)
    x.delete()
    messages.error(request, ' your Cart Deleted!')
    return redirect(cart_page)

def userlogin_page(request):
    return render(request,"userlogin.html")
