
from django.shortcuts import render,redirect
from .models import Products,Cart,CartItem
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage

def home(response):
    # for item in CartItem.objects.all():
    #     Products.objects.get(id=int(item.productid)).delete() deleting items from cart....

    try:
        x=response.user.cart.count()
        
        
        if x  < 1:
            c=Cart()
            c.save()
            response.user.cart.add(c)
    except:
            print("nejde cart")
        

    try:
            
            ls =Products.objects.all
           
            User = get_user_model()
            users = User.objects.all()
            print(users)
    except:
            print("nejde")

    # cart items quantity
    # for cart in response.user.cart.all():
    
    #     number=cart.cartitem_set.count()
    
    return render(response, "main/home.html", {"ls":ls,"users":users})


def userproducts(response):
           
    return render(response, "main/userproducts.html", {})

def addProducts(response):
    if response.method =="POST":
        if response.POST.get("create"):
            name=response.POST.get("name")
            p=Products(name=name)
            p.description = response.POST.get("description")
            p.categories = response.POST.get("category")
            p.size = response.POST.get("size")
            p.price = response.POST.get("price")
            
            img = response.FILES["image"]
            fileSystemStorage=FileSystemStorage()
            fileSystemStorage.save(img.name,img)
            p.image = img.name
            p.checked = False
            p.save()
            response.user.products.add(p)
            

    
    return render(response, "main/addProducts.html", {})
def productLook(response, id):
    pd =Products.objects.get(id=id)
    carts= response.user.cart.all()
    
    for i in carts:
        cart=Cart.objects.get(id= i.id) 
        items=cart.cartitem_set
        quantity=items.filter(productid=pd.id)
        
    
    if response.method =="POST":
        if response.POST.get("addtocart"):
            if len(quantity) == 0:
                productid=pd.id
                name = pd.name
                price= pd.price
                size = pd.size
                image = pd.image
                cart.cartitem_set.create(productid=productid, name=name,price=price, size=size, image=image )
            else:
                pass
            
            
            
    
    return render(response, "main/productLook.html", {"pd":pd})

def cart(response):
    carts= response.user.cart.all()
    
    for i in carts:
        cart=Cart.objects.get(id= i.id) 
        number= cart.cartitem_set.count()
    if response.method =="POST":
        if response.POST.get("delete"):
            itemid=response.POST.get("delete")
            try:
                cart.cartitem_set.get(id=int(itemid)).delete()
            except:
                redirect("/cart/")
            redirect("/cart/")
    return render(response, "main/cart.html", {"number":number})

    
    
