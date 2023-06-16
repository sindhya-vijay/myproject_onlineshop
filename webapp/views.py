from django.shortcuts import render, redirect
from webapp.models import Registerdb, cartdb
from myapp.models import category_db, productdb, contactdb, checkoutdb
from django.contrib import messages

# Create your views here.

def home_page(request):
    return render(request, "home.html")

def Categorypage(request):
    data = category_db.objects.all()
    return render(request, "Category_page.html", {'data':data})

def productpage(request, catname):
    data = category_db.objects.all()
    pro = productdb.objects.filter(Category=catname)
    return render(request, "product_page.html", {'data':data, 'pro':pro})

def singlepage(request, dataid):
    prosingle = productdb.objects.get(id=dataid)
    pro = productdb.objects.all()
    return render(request, "single_product.html", {'prosingle':prosingle, 'pro':pro})

def registration_page(request):
    return  render(request, "Registration_login.html")

def regdata(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        paswd = request.POST.get('password')
        mob = request.POST.get('mobile')
        em =  request.POST.get('email')
        im =  request.FILES['image']
        obj = Registerdb(Username=uname, Password=paswd,Mobile=mob, Email=em, Image=im)
        obj.save()
        messages.success(request, "Registration completed successfully")
        return redirect(registration_page)

def user_login(request):
    if request.method == "POST":
        unme = request.POST.get('username')
        paswd = request.POST.get('password')
        if Registerdb.objects.filter(Username=unme,Password=paswd).exists():
            request.session['username']=unme
            request.session['password']=paswd
            messages.success(request, "Login successfully")
            return redirect(home_page)
        else:
             messages.error(request, "Invalid username or password")
             return redirect(registration_page)

    return redirect(registration_page)

def signout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "successfully logout")
    return redirect("registration_page")

def contactpage(request):
    return render(request, "contact.html")

def contactus(request):
    if request.method == "POST":
        na = request.POST.get('name')
        eml = request.POST.get('email')
        mob = request.POST.get('mobile')
        msg = request.POST.get('message')
        obj = contactdb(Name=na, Email=eml, Mobile=mob, Message=msg)
        obj.save()
        return redirect(contactpage)

def cart_page(request):
    data = cartdb.objects.filter(Username=request.session['username'])
    return render(request, "cart.html", {'data':data})

def cart_data(request):
    if request.method == "POST":
        na = request.POST.get('uname')
        pna = request.POST.get('pname')
        des = request.POST.get('descr')
        qt = request.POST.get('quant')
        prc = request.POST.get('tot')
        obj = cartdb(Username=na, Product=pna,Description=des,Quantity=qt,Price=prc)
        obj.save()
        messages.success(request, "Added to cart")
        return redirect(cart_page)

def cart_delete(request, dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect("cart_page")

def checkout_page(request):
    return render(request, "check_out.html")

def checkout_data(request):
    if request.method == "POST":
        fna = request.POST.get('fname')
        lna = request.POST.get('lname')
        em = request.POST.get('email')
        mob = request.POST.get('mob')
        ad = request.POST.get('address')
        cnt = request.POST.get('country')
        ct = request.POST.get('city')
        st = request.POST.get('state')
        obj = checkoutdb(Firstname=fna,Lastname=lna,Emailid=em,Mobile=mob, Address=ad,Country=cnt,City=ct,State=st)
        obj.save()
        messages.success(request, "Proceed to checkout")
        return redirect(checkout_page)
