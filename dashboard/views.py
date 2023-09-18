from django.shortcuts import render
from managment.models import *
from django.contrib.auth.hashers import check_password
from random import Random
from math import ceil
from django.core.files.storage import FileSystemStorage
# Create your views here.

def login(request):
    if request.method == 'POST':
        # Login
        if request.POST.get("login"):
            email= request.POST.get('email')
            pas = request.POST.get('password')
            loginer = User.objects.filter(email= email)
            if loginer.exists():
                log = User.objects.get(email= email)  
                if check_password(pas,log.password):
                    n=Customers.objects.count()
                    orders=Order.objects.all()
                    tin=sum(o.order_total_price for o in orders)
                    ord=Order.objects.all().count()
                    return render(request, 'dashboard/index.html',{'order':Order.objects.all().order_by('-order_date')[0:5],"u":log,'total_in':tin,'total_ord':ord,"n_cust":n}) # home page
                else:
                    error = "Password is wrong" 
                    return render(request, 'dashboard/admin-login&register.html',{"error":error})
            else:
                error = "Email is not found" 
                return render(request, 'dashboard/admin-login&register.html',{"error":error})
        # Register
        elif request.POST.get("register"):
            if request.POST.get("register"):
                getten_email = request.POST.get('Email')
                getten_phone = request.POST.get('Phone')
                getten_ssn = request.POST.get('SSN')
                agree = request.POST.get('Agreement') 
                dub_email = User.objects.filter(email= getten_email).exists()
                dub_phone = User.objects.filter(phone= getten_phone).exists()
                dub_ssn = User.objects.filter(ssn= getten_ssn).exists()
                esn=request.POST.get('ESN')
                if esn != "32013021":
                    error = "wrong ESN" 
                    return render(request, 'dashboard/admin-login&register.html',{"error2":error,"e":1})
                elif dub_email:
                    error = "Email is used" 
                    return render(request, 'dashboard/admin-login&register.html',{"error2":error,"e":1})
                elif dub_ssn:
                    error = "SSN is used" 
                    return render(request, 'dashboard/admin-login&register.html',{"error2":error,"e":1})
                elif dub_phone:
                    error = "Phone is used" 
                    return render(request, 'dashboard/admin-login&register.html',{"error2":error,"e":1})
                elif not agree:
                    error = "Must agree the terms and conditions" 
                    print(request.POST.get('Gender'))
                    return render(request, 'dashboard/admin-login&register.html',{"error2":error,"e":1})
                else:
                    xf_name = request.POST.get('First Name')
                    xm_name = request.POST.get('Middle Name')
                    xl_name = request.POST.get('Last Name')
                    xemail = request.POST.get('Email')
                    xpassword = request.POST.get('Password2')
                    xphone = request.POST.get('Phone')
                    xbirthdate = request.POST.get('Date')
                    xgender = request.POST.get('Gender')
                    xssn = request.POST.get('SSN')
                    xaddress = request.POST.get('Address')
                    new_User = User(f_name= xf_name,
                                             m_name= xm_name,
                                             l_name= xl_name,
                                             email= xemail,
                                             password= xpassword,
                                             birthdate= xbirthdate,
                                             gender= xgender,
                                             phone= xphone,
                                             ssn= xssn,
                                             address= xaddress,
                                             )
                    
                    new_User.save()
                    n=Customers.objects.count()
                    orders=Order.objects.all()
                    tin=sum(o.order_total_price for o in orders)
                    ord=Order.objects.all().count()
                    return render(request, 'dashboard/index.html',{'order':Order.objects.all().order_by('-order_date')[0:5],"u":new_User,'total_in':tin,'total_ord':ord,"n_cust":n})


    return render(request, 'dashboard/admin-login&register.html')
def dashboard(request,x):
    u=User.objects.get(email= x)
    n=Customers.objects.count()
    orders=Order.objects.all()
    tin=sum(o.order_total_price for o in orders)
    ord=Order.objects.all().count()
    return render(request, 'dashboard\index.html' ,{'order':Order.objects.all().order_by('-order_date')[0:5],"u":u,'total_in':tin,'total_ord':ord,"n_cust":n})#,{'admin':"omar"}
def customer(request,x):
    u=User.objects.get(email= x)
    return render(request, 'dashboard\customers.html',{'customer':Customers.objects.all(),"u":u})#,'admin':admin
def order(request,x):
    u=User.objects.get(email= x)
    return render(request, 'dashboard\orders.html',{'order': Order.objects.all(),"u":u})#,'admin':"omar"
def product(request,x):
    u=User.objects.get(email= x)
    return render(request, 'dashboard\products.html',{'product': Product.objects.all(),"u":u})#,'admin':"omar"
def admin(request,x):
    u=User.objects.get(email= x)
    return render(request, 'dashboard\dmin.html',{'admin': User.objects.all(),"u":u})
def product(request,x):
    u=User.objects.get(email= x)
    return render(request, 'dashboard\product.html',{'product': Product.objects.all(),"u":u})
def profile(request,x,y):
    u=User.objects.get(email= x)
    a=User.objects.get(email= y)
    return render(request, 'dashboard\profile.html',{"u":u,"a":a})
def show(request,x,y):
    if request.method == 'POST' :#request.FILES['image']and 'image' in  and 'image1' in request.FILES and 'image2' in request.FILES
        if request.POST.get("submit") :
            p_id=request.POST.get('pid')
            print(p_id)
            pro=Product.objects.get(id=p_id)
            pro.name = request.POST.get('p_name')
            pro.company_name = request.POST.get('p_co_name')
            pro.manufacture_date = request.POST.get('p_manfacture')
            pro.expired_date = request.POST.get('p_expired')
            pro.supply_date = request.POST.get('p_supply')
            pro.price = request.POST.get('p_price')
            pro.quantity = request.POST.get('p_quantity')
            pro.supplier_name = request.POST.get('p_supplier')
            pro.category = request.POST.get('choices')
            pro.description = request.POST.get('description')
            # pro.name = request.POST.get('p_name')
            # pro.company_name = request.POST.get('p_co_name')
            # pro.manufacture_date = request.POST.get('p_manfacture')
            # pro.expired_date = request.POST.get('p_expired')
            # pro.supply_date = request.POST.get('p_supply')
            # pro.price = request.POST.get('p_price')
            # pro.quantity = request.POST.get('p_quantity')
            # pro.supplier_name = request.POST.get('p_supplier')
            # pro.category = request.POST.get('choices')
            # pro.description = request.POST.get('description')
            pro.save()
            return render(request, 'dashboard\product.html',{'product': Product.objects.all(),"u":User.objects.get(email=x)})
    u=User.objects.get(email= x)
    a=Product.objects.get(id= y)
            
    return render(request, 'dashboard\edit.html',{"u":u,"p":a})
#-------------------------------------------------------------------------------------------------------------------------------------------------
def add(request,x):
    if request.method == 'POST' :#request.FILES['image']and 'image' in  and 'image1' in request.FILES and 'image2' in request.FILES
        if request.POST.get("add") :
                pname = request.POST.get('p_name')
                coname = request.POST.get('p_co_name')
                pmanufacture = request.POST.get('p_manfacture')
                pex = request.POST.get('p_expired')
                psup = request.POST.get('p_supply')
                pprice = request.POST.get('p_price')
                pn = request.POST.get('p_quantity')
                psupplier = request.POST.get('p_supplier')
                pcat = request.POST.get('choices')
                pdisc = request.POST.get('description')
                image = request.FILES.get('image')
                #image1 = request.FILES.get('image1')
                #image2 = request.FILES.get('image2')
#image= request.['image']
                # image2 = request.FILES['image2']
              #  fs = FileSystemStorage()
               # file1 = fs.save(image.name, image)
                #file_url1 = fs.url(file1)
                # file2 = fss.save(image1.name, image1)
                # file_url2 = fss.url(file2)
                # file3 = fss.save(image.name, image2)
                # file_url3 = fss.url(file3)




                rand_id = str(ceil(Random().uniform(a=00000, b= 99999)))
                while Cart.objects.filter(id= rand_id).exists():
                    rand_id = str(Random().uniform(a=00000, b= 99999))
                pro = Product(name= pname,
                                        id= rand_id,
                                        company_name= coname,
                                        price= pprice,
                                        expired_date=pex ,
                                        manufacture_date = pmanufacture,
                                        description=pdisc ,
                                        supplier_name= psupplier,
                                        supply_date=psup,
                                        category=pcat ,
                                       image=image,
                                        quantity=pn,)
#image1=image1, image2=image2)
                
                pro.save()
                return render(request, 'dashboard\product.html',{'product': Product.objects.all(),"u":User.objects.get(email=x)})
    return render(request, 'dashboard/add.html',{"u":User.objects.get(email=x)})