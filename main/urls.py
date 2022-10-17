from . import views
from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static
urlpatterns = [
    path("home/", views.home, name="home"),
    path("myproducts/", views.userproducts, name="myproducts"),
    path("add/", views.addProducts, name="add"),
    path("cart/", views.cart, name="cart"),
    path("<int:id>/", views.productLook, name="look"),
    path("edit-<int:id>/", views.productEdit, name="edit"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)