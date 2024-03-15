from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
import datetime
from cloudinary.models import CloudinaryField


# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     family_name = models.CharField(max_length=50,null=True,blank=True)
#     profile_photo = CloudinaryField('image',blank=True,null=True)
#     hood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # personal_cart= models.ForeignKey(Cart, on_delete=DO_NOTHING,null=True )

#     def save_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     @classmethod
#     def update_profile_photo(cls, id,family_email):
#         return cls.objects.filter(id = id).update(family_email=family_email)

    
#     @classmethod
#     def search_username(cls,search_term):
#         return cls.objects.filter(user__username__icontains = search_term)


#     def get_absolute_url(self):
#         return reverse('profile',args=[str(self.id)])


#     def __str__(self) -> str:
#        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # to save the data
    def register(self):
        self.save()
 
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
 
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
 
        return False

class Category(models.Model):
    name = models.CharField(max_length=50)
 
    def new_category(self):
        self.save()

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
 
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    availability = models.TextField(max_length=20)
    image = CloudinaryField('uploads/products/',blank=True,null=True)


    def new_product(self):
        self.save()
 
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
 
    @staticmethod
    def get_all_products():
        return Product.objects.all()
 
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
        

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default=0, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
 
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')