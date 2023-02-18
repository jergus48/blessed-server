from . import views
from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("home/", views.home, name="home"),
    path("search/", views.SearchResultsView, name="search_results"),
    path("about-us/", views.about_us, name="about_us"),
    path("contact/", views.contact, name="contact"),
    path("terms-and-conditions/", views.FAQ, name="FAQ"),
    path("productcharge/", views.ProductCharge, name="ProductCharge"),
    path("wantedcharge/", views.WantedCharge, name="WantedCharge"),
    path("donationcharge/", views.DonationCharge, name="DonationCharge"),
    path("somethingwentwrong/", views.somethingwentwrong, name="somethingwentwrong"),
    path("succes/<str:args>/", views.succesMsg, name="succes"),
    path("succes/wanted/<str:args>/", views.succesWMsg, name="succeswanted"),
    path("donation/<str:args>/", views.DonationMsg, name="donation"),
    path('ads.txt/', views.ads_txt, name='ads_txt'),
    #products
    path("products/", views.products, name="products"),
    path("myproducts/", views.userproducts, name="myproducts"),
    path("user-<int:id>/products/", views.UsersProducts, name="UsersProducts"),
    path("add/", views.addProducts, name="addProducts"),
    path("<int:id>/", views.productLook, name="productLook"),
    path("edit-<int:id>/", views.productEdit, name="productEdit"),
    path("shoes/", views.shoes, name="shoes"),
    path("clothes/", views.clothes, name="clothes"),
    path("accesories/", views.accesories, name="accesories"),
    # wanted
    path("wanted/", views.wanted, name="wanted"),
    path("mywanted/", views.userwanted, name="mywanted"),
    path("user-<int:id>/wanted/", views.UsersWanted, name="UsersWanted"),
    path("add/wanted/", views.addWanted, name="addWanted"),
    path("w<int:id>/", views.wantedLook, name="wantedLook"),
    path("edit-w<int:id>/", views.wantedEdit, name="wantedEdit"),
    ]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]



     # path("cart/", views.cart, name="cart"),