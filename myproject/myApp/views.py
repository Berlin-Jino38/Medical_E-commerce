from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import Catagory,Product,OrderDetails
from .form import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index_page(request):
    template=loader.get_template('myApp/index.html')
    return HttpResponse(template.render({},request))



def register_page(request):
    if request.method=='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    else:
        form=RegistrationForm()
    return render(request,'myApp/register.html',{'form':form})


def about_us(request):
    template=loader.get_template('myApp/about.html')
    return HttpResponse(template.render({},request))

def contact_page(request):
    template=loader.get_template('myApp/contact.html')
    return HttpResponse(template.render({},request))


@login_required
def category(request):
    catagories =Catagory.objects.all().order_by('name')  
    template=loader.get_template('myApp/category.html')
    return HttpResponse(template.render({'Category':catagories},request))

def product(request):
    products =Product.objects.all().order_by('name')  
    template=loader.get_template('myApp/products.html')
    return HttpResponse(template.render({'products':products},request))

def product(request, name):
    if Catagory.objects.filter(name=name, status=0).exists():
        product = Product.objects.filter(catagory__name=name).order_by('name')  
        template = loader.get_template('myApp/products.html')
        return HttpResponse(template.render({"products": product , "catagory":name}, request))
    else:
        #messages.warning(request, "No such Category found")
        return redirect('category')
    
def logout_view(request):
    return render(request,'myApp/logout.html')


def search_view(request):
    query = request.GET.get('q')
   
    if query:
        items = Catagory.objects.filter(name__icontains=query).order_by('-name')
       
    else:
        # Handle the case when 'q' is not provided, for example, display all categories.
        items = Catagory.objects.all().order_by('-name')  
    return render(request, 'myApp/category.html', {'Category': items})

def search_view1(request):
    query = request.GET.get('q')
   
    if query:
        items = Product.objects.filter(name__icontains=query).order_by('-name')
       
    else:
        # Handle the case when 'q' is not provided, for example, display all categories.
        items = Product.objects.all().order_by('-name')  
    return render(request, 'myApp/products.html', {'products': items})

@login_required
def add_view(request):
    if request.method == 'POST':
        # Get the product name, quantity, and price from the form POST data
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        product_price = request.POST.get('product_price')
        product_id = request.POST.get('product_ide')
        # Create or retrieve the cart from the session
        cart = request.session.get('cart', [])

        # Add the product data to the cart
        cart_item = {
            'product_id':product_id,
            'product_name': product_name,
            'quantity': quantity,
            'product_price': product_price,
        }
        cart.append(cart_item)

        # Store the updated cart back in the session
        request.session['cart'] = cart

    # Retrieve the cart from the session (even if it's empty)
    cart = request.session.get('cart', [])

    return render(request, 'myApp/Add_to_cart.html', {'cart': cart})


from django.shortcuts import redirect

def remove_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')

        # Find and remove the item from the cart
        cart = request.session.get('cart', [])
        updated_cart = [item for item in cart if item['product_id'] != item_id]
        request.session['cart'] = updated_cart

    return redirect('add')  # Redirect back to the cart page

def view_cart(request):
    # Retrieve the cart from the session (even if it's empty)
    cart = request.session.get('cart', [])

    # Calculate the total price
    total_price = sum(int(item['quantity']) * float(item['product_price']) for item in cart)
    return render(request, 'myApp/Add_to_cart.html', {'cart': cart, 'total_price': total_price})

def admin_cart_view(request):
    # Retrieve cart data from the session
    cart = request.session.get('cart', [])
    current_user = request.user
    user_email = request.user.email

    # Iterate through the cart items and save them to the database
    for item in cart:
        name = item.get('product_name')
        quantity = item.get('quantity')
        price = item.get('product_price')

        # Create a new OrderDetails record for each item
        order_detail, created = OrderDetails.objects.get_or_create(
            username=current_user,
            email=user_email,
            Medicine_name=name,
            quantity=quantity,
            price=price
        )

    # Clear the cart in the session after saving to the database
    request.session['cart'] = []

    # Redirect the user to a thank you or confirmation page
    return render(request,'myApp/admin_cart.html')