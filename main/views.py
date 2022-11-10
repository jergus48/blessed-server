
from django.core.mail import send_mail
from unicodedata import category
from django.shortcuts import render,redirect,HttpResponse
from .models import Products, Wanted
from django.contrib.auth.models import User
# Create your views here.

from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q


def home(response):



    try:

            ls =Products.objects.filter(active = True).exclude(user=response.user).order_by('-id')[:10]
            wd =Wanted.objects.filter(active = True).exclude(user=response.user).order_by('-id')[:10]

    except:
            print("nejde")


    return render(response, "main/home.html", {"ls":ls,"wd":wd})
def about_us(response):
    
    return render(response, "main/about_us.html", {})
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        msg=request.POST.get("message")
        email=request.POST.get("email")
        message="Name: "+ name + '\n' + "From Mail: "+email + '\n'+'Message:'+ '\n' +msg
        
        send_mail(name,message,'blessedstore.sk@gmail.com',['blessedstore.sk@gmail.com'])
        return HttpResponse('Email was sent')
    return render(request, "main/contact.html", {})
def FAQ(response):
    
    return render(response, "main/FAQ.html", {})
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
    sizes=["XXS","XS","S","M","L","XL","XXL","3XL","35","36","37","38","39","40","41","42","43","44","45"]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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

            if size == "choosen" or condition=="choosen" or country=="choosen":
                pd=pd.filter(categories__in=c)
            else:
                pd =Products.objects.all().order_by(order).filter(Q(name__icontains=name),active = True,categories__in=c).exclude(user=request.user)

    else:
        # ,price__lte=100
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
    return render(request, "main/SearchResults.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"condition_arrow":condition_arrow,"pd":pd,"name":name,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"sizes":sizes,"x":x,"y":y,"z":z,"c":c,"conditions":conditions,"eu_countries":eu_countries})

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
    sizes=["XXS","XS","S","M","L","XL","XXL","3XL","35","36","37","38","39","40","41","42","43","44","45"]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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

            if size == "choosen" or condition=="choosen" or country=="choosen":
                pd=pd.filter(categories__in=c)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,categories__in=c).exclude(user=request.user)

    else:
        # ,price__lte=100
        pd =Products.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)

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




    return render(request, "main/products/products.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"condition_arrow":condition_arrow,"pd":pd,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"sizes":sizes,"x":x,"y":y,"z":z,"c":c,"conditions":conditions,"eu_countries":eu_countries})
def userproducts(response):
    pd=Products.objects.all().order_by('-id').filter(user=response.user)
    if response.method =="POST":

        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            pd=Products.objects.get(id=int(itemid))
            imageurl=pd.image.url
            pd.delete()
            os.remove('static'+imageurl)

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
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
    shoessize=["35","36","37","38","39","40","41","42","43","44","45"]
    clothessize=["XXS","XS","S","M","L","XL","XXL","3XL"]
    if response.method =="POST":

        if response.POST.get("create"):
            name=response.POST.get("name")
            p=Products(name=name)
            p.description = response.POST.get("description")
            p.categories = response.POST.get("category")

            if p.categories =="Clothes":
                p.size = response.POST.get("sizeC")
            elif p.categories =="Shoes":
                p.size = response.POST.get("sizeS")
            elif p.categories =="Accesories":
                p.size = response.POST.get("sizeA")
            p.price = response.POST.get("price")
            p.condition = response.POST.get("condition")
            p.country = response.POST.get("country")
            p.color1 = response.POST.get("color1")
            p.color2 = response.POST.get("color2")
            p.save()
            img = response.FILES["image"]
            unit= img.name.split(".")[-1]
            fileSystemStorage=FileSystemStorage()
            fileSystemStorage.save(str(p.id)+"."+ unit,img)

            p.image = str(p.id)+"."+ unit
            p.save()
            response.user.products.add(p)



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
    user=User.objects.get(id=id)
    ig=user.last_name.replace("@","")
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    sizes=["XXS","XS","S","M","L","XL","XXL","3XL","35","36","37","38","39","40","41","42","43","44","45"]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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

            if size == "choosen" or condition=="choosen" or country=="choosen":
                pd=pd.filter(categories__in=c)
            else:
                pd =Products.objects.all().order_by(order).filter(active = True,categories__in=c,user=user)

    else:
        # ,price__lte=100
        pd =Products.objects.all().order_by('-id').filter(active = True,user=user)

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




    return render(request, "main/products/UsersProducts.html", {"pd":pd,"choice":choice,"user":user,"ig":ig,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"sizes":sizes,"x":x,"y":y,"z":z,"c":c,"conditions":conditions,"eu_countries":eu_countries})

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
    sizes=["XXS","XS","S","M","L","XL","XXL","3XL","35","36","37","38","39","40","41","42","43","44","45"]

    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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

            if size == "choosen" or country=="choosen":
                wd=wd.filter(categories__in=c)
            else:
                wd =Wanted.objects.all().order_by(order).filter(active = True,categories__in=c).exclude(user=request.user)
    else:
        # ,price__lte=100
        wd =Wanted.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)

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
    return render(request, "main/wanted/wanted.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"categoriescheck":categoriescheck,"size_display":size_display,"country_display":country_display,"categories_display":categories_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"categories_arrow":categories_arrow,"wd":wd,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"c":c,"sizes":sizes,"x":x,"z":z,"eu_countries":eu_countries})
def userwanted(response):
    wd=Wanted.objects.all().order_by('-id').filter(user=response.user)
    if response.method =="POST":

        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            pd=Wanted.objects.get(id=int(itemid))

            imageurl=pd.image.url
            pd.delete()
            if pd.image.url != '/images/blessedimg.jpeg':
                os.remove('static'+imageurl)

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
    choicep="Price up to €"
    pricex=""
    categories=["Shoes","Clothes","Accesories"]
    sizes=["XXS","XS","S","M","L","XL","XXL","3XL","35","36","37","38","39","40","41","42","43","44","45"]

    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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

            if size == "choosen" or country=="choosen":
                wd=wd.filter(categories__in=c)
            else:
                wd =Wanted.objects.all().order_by(order).filter(active = True,categories__in=c,user=user)
    else:
        # ,price__lte=100
        wd =Wanted.objects.all().order_by('-id').filter(active = True,user=user)

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
    return render(request, "main/wanted/UsersWanted.html", {"user":user,"ig":ig,"wd":wd,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"categories":categories,"c":c,"sizes":sizes,"x":x,"z":z,"eu_countries":eu_countries})
def addWanted(response):
    if response.user.is_authenticated == False:
        response = redirect('/login/')
        return response
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
    shoessize=["35","36","37","38","39","40","41","42","43","44","45"]
    clothessize=["XXS","XS","S","M","L","XL","XXL","3XL"]
    if response.method =="POST":

        if response.POST.get("create"):
            name=response.POST.get("name")
            w=Wanted(name=name)

            w.categories = response.POST.get("category")

            if w.categories =="Clothes":
                w.size = response.POST.get("sizeC")
            elif w.categories =="Shoes":
                w.size = response.POST.get("sizeS")
            elif w.categories =="Accesories":
                w.size = response.POST.get("sizeA")
            w.maxprice = response.POST.get("price")
            w.country = response.POST.get("country")
            w.color1 = response.POST.get("color1")
            w.color2 = response.POST.get("color2")
            w.save()

            if response.FILES.get('image'):
                img = response.FILES["image"]
                unit= img.name.split(".")[-1]
                fileSystemStorage=FileSystemStorage()
                fileSystemStorage.save("w"+str(w.id)+"."+ unit,img)

                w.image = "w"+str(w.id)+"."+ unit
                w.save()
            response.user.wanted.add(w)



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
    shoessize=["35","36","37","38","39","40","41","42","43","44","45"]
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
    sizes=["35","36","37","38","39","40","41","42","43","44","45"]
    conditions=["New","9/10","8/10","7/10","6/10","5/10","4/10","3/10","2/10","1/10"]
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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
            shoes =Products.objects.all().order_by(order).filter(categories="shoes",active = True,size__in=x).exclude(user=request.user)
        else:
            shoes =Products.objects.all().order_by(order).filter(categories="shoes",active = True).exclude(user=request.user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                shoes=shoes.filter(condition__in=y)
            else:
                shoes =Products.objects.all().order_by(order).filter(categories="shoes",active = True,condition__in=y).exclude(user=request.user)
        if request.POST.getlist("country"):

            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                shoes=shoes.filter(country__in=z)
            else:
                shoes =Products.objects.all().order_by(order).filter(categories="shoes",active = True,country__in=z).exclude(user=request.user)

    else:
        # ,price__lte=100
        shoes =Products.objects.all().order_by('-id').filter(categories="shoes",active = True).exclude(user=request.user)

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

    return render(request, "main/products/shoes.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"condition_arrow":condition_arrow,"shoes":shoes,"choice":choice,"choicep":choicep,"price":pricex,"order":order,"sizes":sizes,"x":x,"y":y,"z":z,"conditions":conditions,"eu_countries":eu_countries})
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
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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
            clothes =Products.objects.all().order_by(order).filter(categories="clothes",active = True,size__in=x).exclude(user=request.user)
        else:
            clothes =Products.objects.all().order_by(order).filter(categories="clothes",active = True).exclude(user=request.user)
        if request.POST.getlist("condition"):
            condition="choosen"
            y=request.POST.getlist("condition")

            if size == "choosen":
                clothes=clothes.filter(condition__in=y)
            else:
                clothes =Products.objects.all().order_by(order).filter(categories="clothes",active = True,condition__in=y).exclude(user=request.user)
        if request.POST.getlist("country"):

            z=request.POST.getlist("country")

            if size == "choosen" or condition=="choosen":
                clothes=clothes.filter(country__in=z)
            else:
                clothes =Products.objects.all().order_by(order).filter(categories="clothes",active = True,country__in=z).exclude(user=request.user)

    else:
        # ,price__lte=100
        clothes =Products.objects.all().order_by('-id').filter(categories="clothes",active = True).exclude(user=request.user)

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

    return render(request, "main/products/clothes.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"condition_arrow":condition_arrow,"clothes":clothes,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"sizes":sizes,"x":x,"y":y,"z":z,"conditions":conditions,"eu_countries":eu_countries})
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
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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


            accesories =Products.objects.all().order_by(order).filter(categories="accesories",active = True,condition__in=y).exclude(user=request.user)
        else:
            accesories =Products.objects.all().order_by(order).filter(categories="accesories",active = True).exclude(user=request.user)
        if request.POST.getlist("country"):

            z=request.POST.getlist("country")

            if condition=="choosen":
                accesories=accesories.filter(country__in=z)
            else:
                accesories =Products.objects.all().order_by(order).filter(categories="accesories",active = True,country__in=z).exclude(user=request.user)

    else:
        # ,price__lte=100
        accesories =Products.objects.all().order_by('-id').filter(categories="accesories",active = True).exclude(user=request.user)

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

    return render(request, "main/products/accesories.html", {"sizecheck":sizecheck,"countrycheck":countrycheck,"conditioncheck":conditioncheck,"size_display":size_display,"country_display":country_display,"condition_display":condition_display,"size_arrow":size_arrow,"country_arrow":country_arrow,"condition_arrow":condition_arrow,"accesories":accesories,"choice":choice,"order":order,"choicep":choicep,"price":pricex,"y":y,"z":z,"conditions":conditions,"eu_countries":eu_countries})


