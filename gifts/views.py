from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from .models import ItemDetailsgifts ,Items
from plants.models import Cart

# Create your views here.

def showgift(request):
    template = loader.get_template('showgift.html')
    val=request.GET.get('gift')
    if val !='' and val !=None:
        gift=ItemDetailsgifts.objects.filter(nameproduct=val)
    else:
        gift=ItemDetailsgifts.objects.all()
    show_All = bool(val)
    return HttpResponse(template.render({'gift':gift ,'show_All': show_All}))


def detailsgift(request,id):
    template = loader.get_template('detailsgift.html')
    gift=ItemDetailsgifts.objects.all().filter(id=id)
    gift_related=ItemDetailsgifts.objects.all().exclude(id=id)[:3]
    context={
        'gift':gift,
        'gift_related':gift_related
    }
    return HttpResponse(template.render(context))


def add_to_cart_g(request,id):
    currentuser=request.user
    discount=2
    state=False
    g=ItemDetailsgifts.objects.filter(id=id)
    for item in g:
        net=item.total-discount
    cart=Cart(
        Id_product=item.id,
        Id_user=currentuser.id,
        price=item.price,
        qty=item.qty,
        tax=item.tax,
        total=item.total,
        discount=discount,
        net=net,
        status=state,
        image=item.image1,
        name_product=item.nameproduct
    )  
    currentuser=request.user.id
    count=Cart.objects.filter(Id_user=currentuser).count()
    cart.save()
    request.session['countcart']=count
    return redirect('/showgift')