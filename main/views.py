
from django.core.mail import send_mail
from unicodedata import category
from django.shortcuts import render,redirect,HttpResponse
from .models import Products, Wanted
from django.contrib.auth.models import User
# Create your views here.
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
from django.urls import reverse
import stripe
from django.conf import settings


def ProductCharge(request):
    
    if  request.method == 'POST':
        try:
            print('DATa:',request.POST)
            product=request.POST['name']
            # customer = stripe.Customer.create(email=request.user.email,name=request.user.first_name,description=request.POST['name'],source=request.POST['stripeToken'])
            # charge = stripe.Charge.create(customer=customer,amount=100,currency='eur')
            name=request.POST.get("name")
            p=Products(name=name)
            p.description = request.POST.get("description")
            p.categories = request.POST.get("category")

            if p.categories =="Clothes":
                p.size = request.POST.get("sizeC")
            elif p.categories =="Shoes":
                p.size = request.POST.get("sizeS")
            elif p.categories =="Accesories":
                p.size = request.POST.get("sizeA")
            p.price = request.POST.get("price")
            p.condition = request.POST.get("condition")
            p.country = request.POST.get("country")
            p.color1 = request.POST.get("color1")
            p.color2 = request.POST.get("color2")
            p.save()
            img = request.FILES["image"]
            unit= img.name.split(".")[-1]
            fileSystemStorage=FileSystemStorage()
            fileSystemStorage.save(str(p.id)+"."+ unit,img)

            p.image = str(p.id)+"."+ unit
            p.save()
            request.user.products.add(p)
            
        except:
            response = redirect('/somethingwentwrong/')
            return response
    
    return redirect(reverse('succes',args=[product]))
def WantedCharge(request):
    
    if  request.method == 'POST':
        try:
            print('DATa:',request.POST)
            product=request.POST['name']
            # customer = stripe.Customer.create(email=request.user.email,name=request.user.first_name,description=request.POST['name'],source=request.POST['stripeToken'])
            # charge = stripe.Charge.create(customer=customer,amount=100,currency='eur')
            name=request.POST.get("name")
            w=Wanted(name=name)

            w.categories = request.POST.get("category")

            if w.categories =="Clothes":
                w.size = request.POST.get("sizeC")
            elif w.categories =="Shoes":
                w.size = request.POST.get("sizeS")
            elif w.categories =="Accesories":
                w.size = request.POST.get("sizeA")
            w.maxprice = request.POST.get("price")
            w.country = request.POST.get("country")
            w.color1 = request.POST.get("color1")
            w.color2 = request.POST.get("color2")
            w.save()

            if request.FILES.get('image'):
                img = request.FILES["image"]
                unit= img.name.split(".")[-1]
                fileSystemStorage=FileSystemStorage()
                fileSystemStorage.save("w"+str(w.id)+"."+ unit,img)

                w.image = "w"+str(w.id)+"."+ unit
                w.save()
            request.user.wanted.add(w)
            
        except:
            error = redirect('/somethingwentwrong/')
            return error
        
    return redirect(reverse('succeswanted',args=[product]))
def DonationCharge(request):
    
    if  request.method == 'POST':
        amount=request.POST['price']
        
        amount=round(float(amount), 2)
        
        amount=int(amount*100)
        name=request.POST.get("name")
        if request.POST['email']:
            print('DATa:',request.POST)
            customer = stripe.Customer.create(email=request.POST['email'],name=name,source=request.POST['stripeToken'])
            charge = stripe.Charge.create(customer=customer,amount=amount,currency='eur')
            
            email=request.POST['email']
            message="Dear "+ name + ',\n' + "Thank you very much for your donation, we really appreciate that. "'\n'+'Blessed Store'
        
            send_mail('Thank you for your donation',message,'blessedstore.sk@gmail.com',[email])

        else:
            print('DATa:',request.POST)
            
            customer = stripe.Customer.create(name=name,source=request.POST['stripeToken'])
            charge = stripe.Charge.create(customer=customer,amount=amount,currency='eur')

        return redirect(reverse('donation',args=[name]))
def succesMsg(request, args):
    product=args
    return render(request, 'main/succes.html',{'product':product})
def succesWMsg(request, args):
    product=args
    return render(request, 'main/succeswanted.html',{'product':product})
def DonationMsg(request, args):
    name=args
    return render(request, 'main/donation.html',{'name':name})
def somethingwentwrong(request):
    
    return render(request, 'main/somethingwentwrong.html',{})
def home(response):



    try:

            ls =Products.objects.filter(active = True).exclude(user=response.user).order_by('-id')[:10]
            wd =Wanted.objects.filter(active = True).exclude(user=response.user).order_by('-id')[:10]

    except:
            print("nejde")


    return render(response, "main/home.html", {"ls":ls,"wd":wd})
def about_us(response):
    if response.user.is_authenticated == False:
        navbar="False"
    else:
        navbar="True"
    return render(response, "main/about_us.html", {"navbar":navbar})
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        msg=request.POST.get("message")
        email=request.POST.get("email")
        message="Name: "+ name + '\n' + "From Mail: "+email + '\n'+'Message:'+ '\n' +msg
        
        send_mail(name,message,'blessedstore.sk@gmail.com',['blessedstore.sk@gmail.com'])
      
    return render(request, "main/contact.html", {})
def FAQ(response):
    
    return render(response, "main/terms-and-conditions.html", {})
def handler404(request, exception,):
    response=redirect("/")
    return response
def handler500(response):
    
    response=redirect("/")
    return response

def SearchResultsView(request):
    sizecheck=""
    conditioncheck=""
    categoriescheck=""
    countrycheck=""
    categories_display="none"
    condition_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    condition_arrow=0
    categories_arrow=0
    country_arrow=0
    c=[]
    x=[]
    y=[]
    z=[]
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    shoessizes=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessizes=["XXS","XS","S","M","L","XL","XXL","3XL"]
    sizes=[]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.GET.get("name"):
        name = request.GET.get("name")
    elif request.GET.get("brand"):
        name = request.GET.get("brand")
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("conditioncheck"):
        conditioncheck="checked"
        condition_display="block"
        condition_arrow=180
    if request.POST.get("categoriescheck"):
        categoriescheck="checked"
        categories_display="block"
        categories_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        condition="empty"
        category="empty"
        country="empty"
        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            pd =Products.objects.all().order_by(order).filter(Q(name__icontains=name),active = True,size__in=x).exclude(user=request.user)
        else:
            pd =Products.objects.all().order_by(order).filter(Q(name__icontains=name),active = True).exclude(user=request.user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                pd=pd.filter(condition__in=y)
            else:
                pd =Products.objects.all().order_by(order).filter(Q(name__icontains=name),active = True,condition__in=y).exclude(user=request.user)
        if request.POST.getlist("country"):
            country="choosen"
            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                pd=pd.filter(country__in=z)
            else:
                pd =Products.objects.all().order_by(order).filter(Q(name__icontains=name),active = True,country__in=z).exclude(user=request.user)
        if request.POST.getlist("category"):
            category=="choosen"
            c=request.POST.getlist("category")
            if "Clothes" in c:
                sizes=sizes+clothessizes
            if "Shoes" in c:
                sizes=sizes+shoessizes
            
            if size == "choosen" or condition=="choosen" or country=="choosen":
                pd=pd.filter(categories__in=c)
            else:
                pd =Products.objects.all().order_by(order).filter(Q(name__icontains=name),active = True,categories__in=c).exclude(user=request.user)
        else:
            sizes=clothessizes+shoessizes

    else:
        # ,price__lte=100
        sizes=clothessizes+shoessizes
        pd =Products.objects.all().order_by('-id').filter(Q(name__icontains=name),active = True).exclude(user=request.user)

        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                pd=pd.filter(price__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                pd=pd.filter(price__lte=pricex)
                choicep="up to "+str(pricex)+"€"
    paginator = Paginator(pd, 32) 
    count=pd.count()
    page_number = request.GET.get('page')
    pd = paginator.get_page(page_number)
    next2=pd.number + 2
    previous2=pd.number -2  
    return render(request, "main/SearchResults.html", {"count":count,"next2":next2,"previous2":previous2,"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"condition_arrow":condition_arrow,"pd":pd,"name":name,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"sizes":sizes,"x":x,"y":y,"z":z,"c":c,"conditions":conditions,"eu_countries":eu_countries})

 #products
def products(request ):
    sizecheck=""
    conditioncheck=""
    categoriescheck=""
    countrycheck=""
    categories_display="none"
    condition_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    condition_arrow=0
    categories_arrow=0
    country_arrow=0
    c=[]
    x=[]
    y=[]
    z=[]
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    shoessizes=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessizes=["XXS","XS","S","M","L","XL","XXL","3XL"]
    sizes=[]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("conditioncheck"):
        conditioncheck="checked"
        condition_display="block"
        condition_arrow=180
    if request.POST.get("categoriescheck"):
        categoriescheck="checked"
        categories_display="block"
        categories_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        condition="empty"
        category="empty"
        country="empty"
        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            pd =Products.objects.all().order_by(order).filter(active = True,size__in=x).exclude(user=request.user)
        else:
            pd =Products.objects.all().order_by(order).filter(active = True).exclude(user=request.user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                pd=pd.filter(condition__in=y)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,condition__in=y).exclude(user=request.user)
        if request.POST.getlist("country"):
            country="choosen"
            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                pd=pd.filter(country__in=z)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,country__in=z).exclude(user=request.user)
        if request.POST.getlist("category"):
            category=="choosen"
            c=request.POST.getlist("category")
            if "Clothes" in c:
                sizes=sizes+clothessizes
            if "Shoes" in c:
                sizes=sizes+shoessizes
            if size == "choosen" or condition=="choosen" or country=="choosen":
                pd=pd.filter(categories__in=c)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,categories__in=c).exclude(user=request.user)
        else:
            sizes=clothessizes+shoessizes
    else:
        
        pd =Products.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)
        sizes=clothessizes+shoessizes
        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                pd=pd.filter(price__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                pd=pd.filter(price__lte=pricex)
                choicep="up to "+str(pricex)+"€"

   
    paginator = Paginator(pd, 32) 
    count=pd.count()
    page_number = request.GET.get('page')
    pd = paginator.get_page(page_number)
    next2=pd.number + 2
    previous2=pd.number -2  


    return render(request, "main/products/products.html", {"count":count,"next2":next2,"previous2":previous2,"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"condition_arrow":condition_arrow,"pd":pd,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"sizes":sizes,"x":x,"y":y,"z":z,"c":c,"conditions":conditions,"eu_countries":eu_countries})
def userproducts(response):
    pd=Products.objects.all().order_by('-id').filter(user=response.user)
    if response.method =="POST":

        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            pr=Products.objects.get(id=int(itemid))
            
            pr.delete()
            

            # pd.delete()
        else:
            for item in pd:
                  
                  if response.POST.get("p" + str(item.id)) == "on":
                     item.active = True
                     
                    
                  else:
                      item.active = False
                  item.save()


    return render(response, "main/products/userproducts.html", {"pd":pd})

def addProducts(response):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    shoessize=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessize=["XXS","XS","S","M","L","XL","XXL","3XL"]
    # if response.method =="POST":

    #     if response.POST.get("create"):
            


    return render(response, "main/products/addProducts.html", {"eu":eu_countries,"shoessize":shoessize,"clothessize":clothessize})
def productLook(response, id):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    pd =Products.objects.get(id=id)
    ig=pd.user.last_name.replace("@","")


    return render(response, "main/products/productLook.html", {"pd":pd,"ig":ig})
def UsersProducts(request,id):
    if request.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    c=[]
    x=[]
    y=[]
    z=[]
    sizecheck=""
    conditioncheck=""
    categoriescheck=""
    countrycheck=""
    categories_display="none"
    condition_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    condition_arrow=0
    categories_arrow=0
    country_arrow=0
    user=User.objects.get(id=id)
    ig=user.last_name.replace("@","")
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    shoessizes=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessizes=["XXS","XS","S","M","L","XL","XXL","3XL"]
    sizes=[]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("conditioncheck"):
        conditioncheck="checked"
        condition_display="block"
        condition_arrow=180
    if request.POST.get("categoriescheck"):
        categoriescheck="checked"
        categories_display="block"
        categories_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        condition="empty"
        category="empty"
        country="empty"
        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            pd =Products.objects.all().order_by(order).filter(active = True,size__in=x,user=user)
        else:
            pd =Products.objects.all().order_by(order).filter(active = True,user=user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                pd=pd.filter(condition__in=y)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,condition__in=y,user=user)
        if request.POST.getlist("country"):
            country="choosen"
            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                pd=pd.filter(country__in=z)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,country__in=z,user=user)
        if request.POST.getlist("category"):
            category=="choosen"
            c=request.POST.getlist("category")
            if "Clothes" in c:
                sizes=sizes+clothessizes
            if "Shoes" in c:
                sizes=sizes+shoessizes
            if size == "choosen" or condition=="choosen" or country=="choosen":
                pd=pd.filter(categories__in=c)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,categories__in=c,user=user)
        else:
            sizes=clothessizes+shoessizes
    else:
        # ,price__lte=100
        pd =Products.objects.all().order_by('-id').filter(active = True,user=user)
        sizes=clothessizes+shoessizes
        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                pd=pd.filter(price__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                pd=pd.filter(price__lte=pricex)
                choicep="up to "+str(pricex)+"€"




    return render(request, "main/products/UsersProducts.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"condition_arrow":condition_arrow,"pd":pd,"choice":choice,"user":user,"ig":ig,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"sizes":sizes,"x":x,"y":y,"z":z,"c":c,"conditions":conditions,"eu_countries":eu_countries})

def productEdit(response, id):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    edit=str(id).replace("edit-", "")
    pd =Products.objects.get(id=int(edit))
    if response.method =="POST":
        if response.POST.get("change"):

            pd.description = response.POST.get("description")
            pd.price = response.POST.get("price")
            pd.condition = response.POST.get("condition")
            pd.color1 = response.POST.get("color1")
            pd.color2 = response.POST.get("color2")
            pd.save()


    return render(response, "main/products/productEdit.html", {"pd":pd})
#wanted

def wanted(request, ):
    sizecheck=""
    categoriescheck=""
    countrycheck=""
    categories_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    categories_arrow=0
    country_arrow=0
    c=[]
    x=[]
    z=[]
    
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    shoessizes=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessizes=["XXS","XS","S","M","L","XL","XXL","3XL"]
    sizes=[]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("categoriescheck"):
        categoriescheck="checked"
        categories_display="block"
        categories_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        country="empty"
        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-maxprice":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "maxprice":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            wd =Wanted.objects.all().order_by(order).filter(active = True,size__in=x).exclude(user=request.user)
        else:
            wd =Wanted.objects.all().order_by(order).filter(active = True).exclude(user=request.user)

        if request.POST.getlist("country"):
            country="choosen"
            z=request.POST.getlist("country")

            if size == "choosen" :
                wd=wd.filter(country__in=z)
            else:
                wd =Wanted.objects.all().order_by(order).filter(active = True,country__in=z).exclude(user=request.user)
        if request.POST.getlist("category"):
            category=="choosen"
            c=request.POST.getlist("category")
            if "Clothes" in c:
                sizes=sizes+clothessizes
            if "Shoes" in c:
                sizes=sizes+shoessizes
            if size == "choosen" or country=="choosen":
                wd=wd.filter(categories__in=c)
            else:
                wd =Wanted.objects.all().order_by(order).filter(active = True,categories__in=c).exclude(user=request.user)
        else:
            sizes=clothessizes+shoessizes
    else:
        # ,price__lte=100
        wd =Wanted.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)
        sizes=clothessizes+shoessizes
        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                wd=wd.filter(maxprice__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                wd=wd.filter(maxprice__lte=pricex)
                choicep="up to "+str(pricex)+"€"
    paginator = Paginator(wd, 32) 
    count=wd.count()
    page_number = request.GET.get('page')
    wd = paginator.get_page(page_number)
    next2=wd.number + 2
    previous2=wd.number -2  
    return render(request, "main/wanted/wanted.html", {"count":count,"next2":next2,"previous2":previous2,"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"wd":wd,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"c":c,"sizes":sizes,"x":x,"z":z,"eu_countries":eu_countries})
def userwanted(response):
    wd=Wanted.objects.all().order_by('-id').filter(user=response.user)
    if response.method =="POST":

        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            pd=Wanted.objects.get(id=int(itemid))

            
            pd.delete()
            

        else:
            for item in wd:
                  
                  if response.POST.get("w" + str(item.id)) == "on":
                     item.active = True
                     
                    
                  else:
                      item.active = False
                  item.save()


    return render(response, "main/wanted/userwanted.html", {"wd":wd})
def UsersWanted(request,id):
    if request.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    user=User.objects.get(id=id)
    ig=user.last_name.replace("@","")
    c=[]
    x=[]
    z=[]
    sizecheck=""
    categoriescheck=""
    countrycheck=""
    categories_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    categories_arrow=0
    country_arrow=0
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    shoessizes=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessizes=["XXS","XS","S","M","L","XL","XXL","3XL"]
    sizes=[]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("categoriescheck"):
        categoriescheck="checked"
        categories_display="block"
        categories_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        country="empty"
        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-maxprice":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "maxprice":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            wd =Wanted.objects.all().order_by(order).filter(active = True,size__in=x,user=user)
        else:
            wd =Wanted.objects.all().order_by(order).filter(active = True,user=user)

        if request.POST.getlist("country"):
            country="choosen"
            z=request.POST.getlist("country")

            if size == "choosen" :
                wd=wd.filter(country__in=z)
            else:
                wd =Wanted.objects.all().order_by(order).filter(active = True,country__in=z,user=user)
        if request.POST.getlist("category"):
            category=="choosen"
            c=request.POST.getlist("category")
            if "Clothes" in c:
                sizes=sizes+clothessizes
            if "Shoes" in c:
                sizes=sizes+shoessizes
            if size == "choosen" or country=="choosen":
                wd=wd.filter(categories__in=c)
            else:
                wd =Wanted.objects.all().order_by(order).filter(active = True,categories__in=c,user=user)
        else:
            sizes=clothessizes+shoessizes
    else:
        # ,price__lte=100
        sizes=clothessizes+shoessizes
        wd =Wanted.objects.all().order_by('-id').filter(active = True,user=user)
        sizes=shoessizes+clothessizes
        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                wd=wd.filter(maxprice__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                wd=wd.filter(maxprice__lte=pricex)
                choicep="up to "+str(pricex)+"€"
    return render(request, "main/wanted/UsersWanted.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"user":user,"ig":ig,"wd":wd,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"c":c,"sizes":sizes,"x":x,"z":z,"eu_countries":eu_countries})
def addWanted(response):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    shoessize=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessize=["XXS","XS","S","M","L","XL","XXL","3XL"]
    
    return render(response, "main/wanted/addWanted.html", {"eu":eu_countries,"shoessize":shoessize,"clothessize":clothessize})
def wantedLook(response, id):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    wid= str(id).replace("w", "")
    pd =Wanted.objects.get(id=wid)
    ig=pd.user.last_name.replace("@","")




    return render(response, "main/wanted/wantedLook.html", {"pd":pd,"ig":ig})


def wantedEdit(response, id):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    edit=str(id).replace("edit-w", "")
    pd =Wanted.objects.get(id=int(edit))
    shoessize=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    clothessize=["XXS","XS","S","M","L","XL","XXL","3XL"]
    
    if response.method =="POST":
        if response.POST.get("change"):
            if pd.categories == "Shoes":
                pd.size=response.POST.get("sizeS")
            elif pd.categories == "Clothes":
                pd.size=response.POST.get("sizeC")
            elif pd.categories == "Accesories":
                pd.size=response.POST.get("sizeA")

            pd.maxprice = response.POST.get("price")

            pd.color1 = response.POST.get("color1")
            pd.color2 = response.POST.get("color2")
            pd.save()





    return render(response, "main/wanted/wantedEdit.html", {"pd":pd,"shoessize":shoessize,"clothessize":clothessize})


#product categories
def shoes(request):
    sizecheck=""
    conditioncheck=""
    countrycheck=""
    condition_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    condition_arrow=0
    country_arrow=0
    x=[]
    y=[]
    z=[]
    choicep="Price up to €"
    pricex=""
    sizes=["35","35,5","36","36,5","37","37,5","38","38,5","39","39,5","40","40,5","41","41,5","42","42,5","43","43,5","44","44,5","45","45,5","46","46,5","47"]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("conditioncheck"):
        conditioncheck="checked"
        condition_display="block"
        condition_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        condition="empty"

        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            shoes =Products.objects.all().order_by(order).filter(categories="Shoes",active = True,size__in=x).exclude(user=request.user)
        else:
            shoes =Products.objects.all().order_by(order).filter(categories="Shoes",active = True).exclude(user=request.user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                shoes=shoes.filter(condition__in=y)
            else:
                shoes =Products.objects.all().order_by(order).filter(categories="Shoes",active = True,condition__in=y).exclude(user=request.user)
        if request.POST.getlist("country"):

            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                shoes=shoes.filter(country__in=z)
            else:
                shoes =Products.objects.all().order_by(order).filter(categories="Shoes",active = True,country__in=z).exclude(user=request.user)

    else:
        # ,price__lte=100
        shoes =Products.objects.all().order_by('-id').filter(categories="Shoes",active = True).exclude(user=request.user)

        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                shoes=shoes.filter(price__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                shoes=shoes.filter(price__lte=pricex)
                choicep="up to "+str(pricex)+"€"
    paginator = Paginator(shoes, 32) 
    count=shoes.count()
    page_number = request.GET.get('page')
    shoes = paginator.get_page(page_number)
    next2=shoes.number + 2
    previous2=shoes.number -2  
    return render(request, "main/products/shoes.html", {"count":count,"next2":next2,"previous2":previous2,"sizecheck":sizecheck,"countrycheck":countrycheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"condition_arrow":condition_arrow,"pd":shoes,"choice":choice,"choicep":choicep,"price":pricex,"order":order,"sizes":sizes,"x":x,"y":y,"z":z,"conditions":conditions,"eu_countries":eu_countries})
def clothes(request):
    sizecheck=""
    conditioncheck=""
    countrycheck=""
    condition_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    condition_arrow=0
    country_arrow=0
    x=[]
    y=[]
    z=[]
    choicep="Price up to €"
    pricex=""
    sizes=["XXS","XS","S","M","L","XL","XXL","3XL"]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("conditioncheck"):
        conditioncheck="checked"
        condition_display="block"
        condition_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("order_by"):

        size="empty"
        condition="empty"

        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        if request.POST.getlist("size"):
            size="choosen"
            x=request.POST.getlist("size")
            clothes =Products.objects.all().order_by(order).filter(categories="Clothes",active = True,size__in=x).exclude(user=request.user)
        else:
            clothes =Products.objects.all().order_by(order).filter(categories="Clothes",active = True).exclude(user=request.user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                clothes=clothes.filter(condition__in=y)
            else:
                clothes =Products.objects.all().order_by(order).filter(categories="Clothes",active = True,condition__in=y).exclude(user=request.user)
        if request.POST.getlist("country"):

            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                clothes=clothes.filter(country__in=z)
            else:
                clothes =Products.objects.all().order_by(order).filter(categories="Clothes",active = True,country__in=z).exclude(user=request.user)

    else:
        # ,price__lte=100
        clothes =Products.objects.all().order_by('-id').filter(categories="Clothes",active = True).exclude(user=request.user)

        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                clothes=clothes.filter(price__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                clothes=clothes.filter(price__lte=pricex)
                choicep="up to "+str(pricex)+"€"
    paginator = Paginator(clothes, 32) 
    count=clothes.count()
    page_number = request.GET.get('page')
    clothes = paginator.get_page(page_number)
    next2=clothes.number + 2
    previous2=clothes.number -2  
    return render(request, "main/products/clothes.html", {"count":count,"next2":next2,"previous2":previous2,"sizecheck":sizecheck,"countrycheck":countrycheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"condition_arrow":condition_arrow,"pd":clothes,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"sizes":sizes,"x":x,"y":y,"z":z,"conditions":conditions,"eu_countries":eu_countries})
def accesories(request):
    sizecheck=""
    conditioncheck=""
    countrycheck=""
    condition_display="none"
    size_display="none"
    country_display="none"
    size_arrow=0
    condition_arrow=0
    country_arrow=0
    y=[]
    z=[]
    choicep="Price up to €"
    pricex=""

    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czechia", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark","England", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg","Monaco", "Netherlands","Norway", "Poland", "Portugal", "Romania","Scotland", "Slovenia", "Spain", "Sweden","Switzerland","Wales"]
    if request.POST.get("sizecheck"):
        sizecheck="checked"
        size_display="block"
        size_arrow=180
    if request.POST.get("conditioncheck"):
        conditioncheck="checked"
        condition_display="block"
        condition_arrow=180
    if request.POST.get("countrycheck"):
        countrycheck="checked"
        country_display="block"
        country_arrow=180
    if request.POST.get("order_by"):


        condition="empty"

        order = request.POST.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"

        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")


            accesories =Products.objects.all().order_by(order).filter(categories="Accesories",active = True,condition__in=y).exclude(user=request.user)
        else:
            accesories =Products.objects.all().order_by(order).filter(categories="Accesories",active = True).exclude(user=request.user)
        if request.POST.getlist("country"):

            z=request.POST.getlist("country")

            if condition=="choosen":
                accesories=accesories.filter(country__in=z)
            else:
                accesories =Products.objects.all().order_by(order).filter(categories="Accesories",active = True,country__in=z).exclude(user=request.user)

    else:
        # ,price__lte=100
        accesories =Products.objects.all().order_by('-id').filter(categories="Accesories",active = True).exclude(user=request.user)

        choice="Latest products"
        order="-id"
    if request.POST.get("pricemax"):

        pricex=request.POST.get("pricemax")
        pricex=int(pricex)
        list=[0,100,200,500,1000,2000,2001]

        if list.count(pricex) == 1:
            if pricex == 2001:
                accesories=accesories.filter(price__gte=2000)
                choicep="from 2000€"
            elif pricex == 0:

                choicep="Price up to €"
            else:
                accesories=accesories.filter(price__lte=pricex)
                choicep="up to "+str(pricex)+"€"
    paginator = Paginator(accesories, 32) 
    count=accesories.count()
    page_number = request.GET.get('page')
    accesories = paginator.get_page(page_number)
    next2=accesories.number + 2
    previous2=accesories.number -2  
    return render(request, "main/products/accesories.html", {"count":count,"next2":next2,"previous2":previous2,"sizecheck":sizecheck,"countrycheck":countrycheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"condition_arrow":condition_arrow,"pd":accesories,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"y":y,"z":z,"conditions":conditions,"eu_countries":eu_countries})


