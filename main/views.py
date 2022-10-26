
from asyncio.windows_events import NULL
from itertools import product
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Products, Wanted
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
from django.views.generic import TemplateView, ListView

def home(response):
   
        

    try:
            
            ls =Products.objects.filter(active = True).exclude(user=response.user).order_by('-id')[:10]
            wd =Wanted.objects.filter(active = True).exclude(user=response.user).order_by('-id')[:10]
            
    except:
            print("nejde")

    
    return render(response, "main/home.html", {"ls":ls,"wd":wd})
def error(response):
    redirect("/")
    return render(response, "404.html", {})



def SearchResultsView(request):
        if request.GET.get("name"):
            name = request.GET.get("name")
        elif request.GET.get("brand"):
            name = request.GET.get("brand")
        if request.GET.get("order_by"):
            order = request.GET.get("order_by")
            if order == "-id":
                    choice="Latest products"
            elif order == "-price":
                    choice="Highest price"
            elif order == "id":
                    choice="Oldest products"
            elif order == "price":
                    choice="Lowest price"
            object_list = Products.objects.filter( Q(name__icontains=name),
                    active=True).exclude(user=request.user).order_by(order)
            return render(request, "main/filters.html", {"object_list":object_list,"choice":choice,"name":name})
        else:
            object_list = Products.objects.filter(Q(name__icontains=name),
                active=True
            ).exclude(user=request.user).order_by("-id")
            choice="Latest products"
        return render(request, "main/SearchResults.html", {"object_list":object_list,"name":name,"choice":choice})
def FiltersView(request):
   
    order = request.GET.get("order_by")
    if order == "-id":
            choice="Latest products"
    elif order == "-price":
            choice="Highest price"
    elif order == "id":
            choice="Oldest products"
    elif order == "price":
            choice="Lowest price"
    if request.GET.get("name"):
        name=request.GET.get("name")
        if name != "":
            object_list = Products.objects.filter( Q(name__icontains=name),
                active=True).exclude(user=request.user).order_by(order)
            return render(request, "main/filters.html", {"object_list":object_list,"choice":choice,"name":name})
    else:
        object_list = Products.objects.filter(
            active=True# Q(name__icontains=query),
        ).exclude(user=request.user).order_by(order)
        return render(request, "main/filters.html", {"object_list":object_list,"choice":choice})
 #products       
def products(request ):
    
    if request.GET.get("order_by"):
        order = request.GET.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        pd =Products.objects.all().order_by(order).filter(active = True).exclude(user=request.user)
        
    else:
        pd =Products.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)
        choice="Latest products"
    
    return render(request, "main/products/products.html", {"pd":pd,"choice":choice})
def userproducts(response):
    pd=Products.objects.all().order_by('-id').filter(user=response.user,active = True)
    if response.method =="POST":
       
        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            pd=Products.objects.get(id=int(itemid))
            imageurl=pd.image.url
            pd.delete()
            os.remove('static'+imageurl)
           
            # pd.delete()
            
            
    return render(response, "main/products/userproducts.html", {"pd":pd})

def addProducts(response):
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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
            

    
    return render(response, "main/products/addProducts.html", {"eu":eu_countries})
def productLook(response, id):
    pd =Products.objects.get(id=id)
    ig=pd.user.last_name.replace("@","")
    
    
    return render(response, "main/products/productLook.html", {"pd":pd,"ig":ig})


def productEdit(response, id):
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
    wd =Wanted.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)
    if request.GET.get("order_by"):
        order = request.GET.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-maxprice":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "maxprice":
                choice="Lowest price"
        wd =Wanted.objects.all().order_by(order).filter(active = True).exclude(user=request.user)
        
    else:
        wd =Wanted.objects.all().order_by('-id').filter(active = True).exclude(user=request.user)
        choice="Latest Wanted products"
    
    return render(request, "main/wanted/wanted.html", {"wd":wd,"choice":choice})    
def userwanted(response):
    if response.method =="POST":
       
        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            pd=Wanted.objects.get(id=int(itemid))
            
            imageurl=pd.image.url
            pd.delete()
            if pd.image.url != '/images/blessedimg.jpeg':
                os.remove('static'+imageurl)
           
            # pd.delete()
            
            
    return render(response, "main/wanted/userwanted.html", {})

def addWanted(response):
    eu_countries = [ "Slovakia", "Czech Republic", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary"
        , "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovenia", "Spain", "Sweden"]
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
            

    
    return render(response, "main/wanted/addWanted.html", {"eu":eu_countries})
def wantedLook(response, id):
    wid= str(id).replace("w", "")
    pd =Wanted.objects.get(id=wid)
    ig=pd.user.last_name.replace("@","")
            
            
            
    
    return render(response, "main/wanted/wantedLook.html", {"pd":pd,"ig":ig})


def wantedEdit(response, id):
    edit=str(id).replace("edit-w", "")
    pd =Wanted.objects.get(id=int(edit))
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

            



    return render(response, "main/wanted/wantedEdit.html", {"pd":pd})    


#product categories
def shoes(request):
    
    if request.GET.get("order_by"):
        order = request.GET.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        shoes=Products.objects.order_by(order).filter(categories="shoes",active = True).exclude(user=request.user)
        
    else:
        shoes=Products.objects.order_by('-id').filter(categories="shoes",active = True).exclude(user=request.user)
        choice="Latest products"
            
            
    return render(request, "main/products/shoes.html", {"shoes":shoes,"choice":choice})
def clothes(request):
   
    if request.GET.get("order_by"):
        order = request.GET.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        clothes=Products.objects.order_by(order).filter(categories="clothes",active = True).exclude(user=request.user)
        
    else:
        clothes=Products.objects.order_by('-id').filter(categories="clothes",active = True).exclude(user=request.user)
        choice="Latest products"
        
           
            
            
    return render(request, "main/products/clothes.html", {"clothes":clothes,"choice":choice})
def accesories(request):
    if request.GET.get("order_by"):
        order = request.GET.get("order_by")
        if order == "-id":
                choice="Latest products"
        elif order == "-price":
                choice="Highest price"
        elif order == "id":
                choice="Oldest products"
        elif order == "price":
                choice="Lowest price"
        accesories=Products.objects.order_by(order).filter(categories="accesories",active = True).exclude(user=request.user)
        
    else:
        accesories=Products.objects.order_by('-id').filter(categories="accesories",active = True).exclude(user=request.user)
        choice="Latest products"
        
           
            
            
    return render(request, "main/products/accesories.html", {"accesories":accesories,"choice":choice})







# def cart(response):
#     carts= response.user.cart.all()
    
#     for i in carts:
#         cart=Cart.objects.get(id= i.id) 
#         number= cart.cartitem_set.count()
#     if response.method =="POST":
#         if response.POST.get("delete"):
#             itemid=response.POST.get("delete")
#             try:
#                 cart.cartitem_set.get(id=int(itemid)).delete()
#             except:
#                 redirect("/cart/")
#             redirect("/cart/")
#     return render(response, "main/cart.html", {"number":number})

# home
#  # for item in CartItem.objects.all():
    #     Products.objects.get(id=int(item.productid)).delete() deleting items from cart....

    # try:
    #     x=response.user.cart.count()
        
        
    #     if x  < 1:
    #         c=Cart()
    #         c.save()
    #         response.user.cart.add(c)
    # except:
    #         print("nejde cart")
    
    # cart items quantity
    # for cart in response.user.cart.all():
    
    #     number=cart.cartitem_set.count()

    #look


    # carts= response.user.cart.all()
    
    # for i in carts:
    #     cart=Cart.objects.get(id= i.id) 
    #     items=cart.cartitem_set
    #     quantity=items.filter(productid=pd.id)
        
    
    # if response.method =="POST":
    #     if response.POST.get("addtocart"):
    #         if len(quantity) == 0:
    #             productid=pd.id
    #             name = pd.name
    #             price= pd.price
    #             size = pd.size
    #             image = pd.image
    #             # cart.cartitem_set.create(productid=productid, name=name,price=price, size=size, image=image )
    #         else:
    #             pass