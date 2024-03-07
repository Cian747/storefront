from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/',views.register_user,name="signup"),
    # path('/login',name="login"),
    # path('/cart',name="cart"),
    # path('/store-inventory',name='inventory'), should just show all the available products
    # path('',name='')


    # path('signup', Signup.as_view(), name='signup'),
    # path('login', Login.as_view(), name='login'),
    # path('logout', logout, name='logout'),
    # path('cart', auth_middleware(Cart.as_view()), name='cart'),
    # path('check-out', CheckOut.as_view(), name='checkout'),
    # path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    # path('/admin', admin.site.urls)
 

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)