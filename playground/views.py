from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import RegistrationForm
from .models import Customer,Category,Product,Order
from django.contrib import messages

# Create your views here.

def home(request):
    
    x = 1
    y = 2
    title = "Storefront"
    context = {
        "title":title
    }
    return render(request,'index.html', context)

def login_user(request):
    '''
    Login for a regular. If the user is a superuser then the get access to admin portal and different views
    '''
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')

def register_user(request):
    '''
    Normal user registration.
    '''
    rgf =RegistrationForm()
    if request.method == 'POST':
        rgf = RegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            user_profile = Customer.objects.get(user = request.user)
            messages.success(request, 'Account was created for ' + user)
            return redirect("login_user")

        context = {
            'rgf': rgf
            }
    return render(request, 'registration/signup.html', {'rgf': rgf})

# def product(request):
#     '''
#     View all the products.
#     '''
#     return render(request, 'registration/register.html')

# def product_detail(request,id):
#     '''
#     View a specific product in detail, using the id as an argument.
#     Thee will be a possibility of viewing comments
#     '''
#     return render(request, 'registration/product-detail.html')


# def cart(request):
#     '''
#     See a specific user cart selection.
#     '''
#     return render(request, 'cart.html')

# def checkout(request):
#     '''
#     Redirection to the payment portal.
#     '''
#     return render(request, 'checkout.html')

