from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def post_save_create_customer_profile(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)