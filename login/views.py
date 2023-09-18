from django.shortcuts import render
from managment.models import User, Customers, Cart
from random import Random
from math import ceil
from django.contrib.auth.hashers import check_password

# Create your views here.

def index(request):
    if request.method == 'POST':
        # Login
        if request.POST.get("login"):
            email= request.POST.get('email')
            pas = request.POST.get('password')
            loginer = Customers.objects.filter(email= email)
            if loginer.exists():
                log = Customers.objects.get(email= email)  
                if check_password(pas,log.password):
                    error = "Correct"
                    return render(request, 'store/login/login&register.html',{"error":error}) # home page
                else:
                    error = "Password is wrong" 
                    return render(request, 'store/login/login&register.html',{"error":error})
            else:
                error = "Email is not found" 
                return render(request, 'store/login/login&register.html',{"error":error})
        # Register
        elif request.POST.get("register"):
                getten_email = request.POST.get('Email')
                getten_phone = request.POST.get('Phone')
                getten_ssn = request.POST.get('SSN')
                agree = request.POST.get('Agreement') 
                dub_email = Customers.objects.filter(email= getten_email).exists()
                dub_phone = Customers.objects.filter(phone= getten_phone).exists()
                dub_ssn = Customers.objects.filter(ssn= getten_ssn).exists()
                if dub_email:
                    error = "Email is used" 
                    return render(request, 'store/login/login&register.html',{"error2":error,"e":1})
                elif dub_ssn:
                    error = "SSN is used" 
                    return render(request, 'store/login/login&register.html',{"error2":error,"e":1})
                elif dub_phone:
                    error = "Phone is used" 
                    return render(request, 'store/login/login&register.html',{"error2":error,"e":1})
                elif not agree:
                    error = "Must agree the terms and conditions" 
                    return render(request, 'store/login/login&register.html',{"error2":error,"e":1})
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
                    rand_id = str(ceil(Random().uniform(a=00000, b= 99999)))
                    print(rand_id)
                    while Cart.objects.filter(id= rand_id).exists():
                        rand_id = str(Random().uniform(a=00000, b= 99999))
                    cart = Cart(id= rand_id)
                    cart.save()
                    new_customer = Customers(f_name= xf_name,
                                             m_name= xm_name,
                                             l_name= xl_name,
                                             email= xemail,
                                             password= xpassword,
                                             birthdate= xbirthdate,
                                             gender= xgender,
                                             phone= xphone,
                                             ssn= xssn,
                                             address= xaddress,
                                             cart_id = cart.id)
                    
                    new_customer.save()
                    # print(request.POST.get('Date'))
                    
                    return render(request, 'store/login/login&register.html')


    return render(request, 'store/login/login&register.html',{"error2":"","error":""})