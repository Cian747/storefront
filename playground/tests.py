from django.test import TestCase,TransactionTestCase
from django.contrib.auth.models import User
from .models import Customer,Category,Order, Product

# Create your tests here.

class TestStorefrontCase(TestCase):
    
    def setUp(self):
        '''
        Create an test all your classes before you work on the application logic
        '''
        self.new_user = User(id = 1, first_name = 'James', last_name = 'Bond', username = 'jamie', email = 'jamesbond@gmail.com')
        self.new_user.save()

        self.new_customer = Customer(id = 1, user = self.new_user, first_name = 'James', last_name = 'Bond',email = 'jamesbond@gmail.com', profile_photo='image.jpg', phone = '070002992', password='user1234')
        self.new_customer.register()

        self.new_category = Category(id = 1, name = 'Test')
        self.new_category.new_category()

        self.new_product = Product(id = 1, name = 'Bag',price = 20, category = self.new_category , description = "A product engineered for you", availability='Available', image='image.jpg')
        self.new_product.new_product()

        self.new_order = Order(id = 1, product= self.new_product, customer = self.new_customer, quantity = 5, total_price = 200, address= 'yokopoko lane' , phone = '070002992' ,date = '2024-03-24', status='True')
        self.new_order.placeOrder()


    def tearDown(self):
        User.objects.all().delete()
        Customer.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Order.objects.all().delete()

    def test_instance_customer(self):
        self.assertTrue(isinstance(self.new_customer, Customer))

    def test_instance_product(self):
        self.assertTrue(isinstance(self.new_product, Product))

    def test_instance_category(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_instance_order(self):
        self.assertTrue(isinstance(self.new_order, Order))


    def test_save_profile(self):
        self.new_customer.register()
        customer = Customer.objects.all()
        self.assertTrue(len(customer) > 0)

    def test_save_product(self):
        self.new_product.new_product()
        product = Product.objects.all()
        self.assertTrue(len(product) > 0)

    def test_save_category(self):
        self.new_category.new_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_save_order(self):
        self.new_order.placeOrder()
        order = Order.objects.all()
        self.assertTrue(len(order) > 0)