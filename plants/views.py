from ipaddress import summarize_address_range
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,Cart,Order,invoice
from .forms import CheckoutForm, CreateUserForm ,LoginUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def showplant(request):
    template = loader.get_template('showplant.html')
    val=request.GET.get('plant')
    if val !='' and val !=None:
        plant=ItemDetails.objects.filter(nameproduct=val)
    else:
        plant=ItemDetails.objects.all()
    show_All = bool(val)
    return HttpResponse(template.render({'plant':plant ,'show_All': show_All}))


def detailsplant(request,id):
    template = loader.get_template('detailsplant.html')
    plant=ItemDetails.objects.all().filter(id=id)
    plant_related=ItemDetails.objects.all().exclude(id=id)[:3]
    context={
        'plant':plant,
        'plant_related':plant_related
    }
    return HttpResponse(template.render(context))


def auth_login(request):
    template = loader.get_template('auth_login.html')
    return HttpResponse(template.render())



@csrf_exempt
def auth_register(request):
    template = loader.get_template('auth_register.html')
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))

@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
    context={'form':form}
    return render(request,'auth_login.html',context)


@csrf_exempt
def auth_logout(request):
    if request.method=="POST" :
        logout(request)
        return redirect("/")
    

@login_required(login_url='/auth_login/')
@csrf_exempt
def checkout(request):
    cart_product=Cart.objects.all()
    total_sum = 0
    price_sum = 0
    for item in  cart_product:
        total_sum += item.total
        price_sum += item.price
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return render(request,'success.html',{'form': form ,'cart_product':cart_product,'total_sum':total_sum,'price_sum': price_sum })
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html',{'form': form ,'cart_product':cart_product,'total_sum':total_sum,'price_sum': price_sum})


def add_to_cart(request,id):
    currentuser=request.user
    discount=2
    state=False
    plant=ItemDetails.objects.filter(id=id)
    for item in plant:
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
    return redirect('showPlant/')




@login_required(login_url='/auth_login/')
def show_cart(request):
    template = loader.get_template('showCart.html')
    cart_product=Cart.objects.all()
    total_sum = 0
    price_sum = 0
    for item in  cart_product:
        total_sum += item.total
        price_sum += item.price
    conttext={
        'cart':cart_product,
        'total_sum':total_sum,
        'price_sum':price_sum,
        'tax':item.tax
    }
    return HttpResponse(template.render(conttext))

def delete_cart(request,id):
    product=Cart.objects.get(id=id)
    product.delete()
    return redirect('/showCart')

def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render())
























