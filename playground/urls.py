from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    # path('/login',name="login"),
    # path('/register',name="register"),
    # path('/cart',name="cart"),
    # path('/store-inventory',name='inventory'), should just show all the available products
    # path('',name='')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)