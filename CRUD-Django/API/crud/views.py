import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.urls import reverse
from dotenv import load_dotenv
from .connectionOddo import connectionOddo

# Create your views here.
def index(request):
    
    odoo = connectionOddo()
    
    products =  odoo.models.execute_kw(odoo.db,odoo.uid,odoo.password,
    'product.template','search_read',
        [
            [
                
                [ "company_id" ,"=", 2   ]
                # [ "id" ,"=", 2]
            ]
        ],
        {'fields': ["name", "list_price", "default_code","description_picking"]}
    )
 

    return render(request, "crud/index.html", {"abarrotes": products})




def create(request):

    if request.method == 'POST':
       

        return HttpResponseRedirect (reverse("index"))

    return render(request, "crud/create.html")

def getproducts(self):
        products = self.models.execute_kw(self.db, self.uid, self.password,
        'product.template', 'search_read',
        [
            [
                ['company_id', '=', 1]
            ]
        ],
        {'fields': ["name", "company_id"]}
        )

        for item in products:
            print("%s -- %s" % (item["name"], item["company_id"][1]))