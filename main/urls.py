from . import views
from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static
urlpatterns = [
    path("home/", views.home, name="home"),
   path("search/", views.SearchResultsView, name="search_results"),
   path("filters/", views.FiltersView, name="filters"),
    #products
    path("products/", views.products, name="products"),
    path("myproducts/", views.userproducts, name="myproducts"),
    path("add/", views.addProducts, name="add"),
    path("<int:id>/", views.productLook, name="look"),
    path("edit-<int:id>/", views.productEdit, name="edit"),
    path("shoes/", views.shoes, name="shoes"),
    path("clothes/", views.clothes, name="clothes"),
    path("accesories/", views.accesories, name="accesories"),
    # wanted
    path("wanted/", views.wanted, name="wanted"),
    path("mywanted/", views.userwanted, name="mywanted"),
    path("add/wanted/", views.addWanted, name="add"),
    path("w<int:id>/", views.wantedLook, name="look"),
    path("edit-w<int:id>/", views.wantedEdit, name="edit"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


     # path("cart/", views.cart, name="cart"),