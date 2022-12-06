from django.contrib.sitemaps import Sitemap
from .models import  Products,Wanted
from django.urls import reverse
class ProductsSitemap(Sitemap):
     changefreq = "hourly"
     priority = 0.9
     protocol = 'https'
     def items(self) :
         return Products.objects.all()
class WantedSitemap(Sitemap):
             protocol = 'https'
             changefreq = "hourly"
             priority = 0.9

             def items(self) :
                 return Wanted.objects.all()
class StaticViewsSitemap(Sitemap):
         protocol = 'https'
         changefreq = "yearly"
         priority = 0.9
    
         def items(self) :
             return ['about_us','contact','FAQ']
         def location(self,item):
             return reverse(item)
class ActiveViewsSitemap(Sitemap):
         protocol = 'https'
         changefreq = "always"
         priority = 0.9
    
         def items(self) :
             return ['search_results','home','products','myproducts','addProducts','shoes','clothes','accesories','wanted','mywanted','addWanted']
         def location(self,item):
             return reverse(item)