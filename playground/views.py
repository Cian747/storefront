from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    
    x = 1
    y = 2
    title = "Storefront"
    context = {
        "title":title
    }
    return render(request,'index.html', context)

# def login_user(request):
#     '''
#     Login for a regular. If the user is a superuser then the get access to admin portal and different views
#     '''
#     return render(request, 'registration/login.html')

# def register_user(request):
#     '''
#     Normal user registration.
#     '''
#     return render(request, 'registration/register.html')

# def cart(request):
#     '''
#     Normal user registration.
#     '''
#     return render(request, 'cart.html')

# def checkout(request):
#     '''
#     Redirection to the payment portal.
#     '''
#     return render(request, 'checkout.html')

# def commenting(request):
#   '''
#   commenting on specific products
#   '''
#   return render(request, 'index.html')

