from django.shortcuts import render
from django.http import HttpResponse, response
from  .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSl = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSl), nSl])


    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    if query in item.desc or query in item.product_name or query in item.category:
        return True
    else:
        return False

def Search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSl = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSl), nSl])

    params = {'allProds': allProds, "msg":""}
    if len(allProds) == 0 or len(query)<2:
        params = {'msg': "Please Make Sure To Enter Relavant Search Query"}

    return render(request, 'shop/search.html', params)


def AboutUs(request):
    return render(request, 'shop/about.html')



def ContactUs(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})

def Tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "itemsJson": order[0].item_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')



def Cart(request):
    return render(request, 'shop/cart.html')

def ProductView(request,pid):
    product = Product.objects.filter(id=pid)
    return render(request, 'shop/productview.html', {'product':product[0]})
    print(product)


def Payment(request):
    return render(request, 'shop/payment.html')
    
def CheckOut(request):

    if request.method=="POST":
        item_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(item_json=item_json, name=name, email=email, phone=phone, address=address, state=state, zip_code=zip_code, city=city, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order Hasbeen placed successfully")
        update.save()
        thank =True
        id = order.order_id
        return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
        

    return render(request, 'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    pass

