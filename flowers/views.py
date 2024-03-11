from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from .models import ItemDetailsflowers 
from plants.models import Cart
# Create your views here.

def showflower(request):
    template = loader.get_template('showflower.html')
    val=request.GET.get('flower')
    if val !='' and val !=None:
        flower=ItemDetailsflowers.objects.filter(nameproduct=val)
    else:
        flower=ItemDetailsflowers.objects.all()
    show_All = bool(val)
    return HttpResponse(template.render({'flower':flower ,'show_All': show_All}))



def detailsflower(request,id):
    template = loader.get_template('detailsflower.html')
    flower=ItemDetailsflowers.objects.all().filter(id=id)
    flower_related=ItemDetailsflowers.objects.all().exclude(id=id)[:3]
    context={
        'flower':flower,
        'flower_related':flower_related
    }
    return HttpResponse(template.render(context))

def add_to_cart_f(request,id):
    currentuser=request.user
    discount=2
    state=False
    f=ItemDetailsflowers.objects.filter(id=id)
    for item in f:
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
    return redirect('/showflower')

