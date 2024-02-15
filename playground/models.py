from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=50,null=True,blank=True)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    # hood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # personal_cart= models.ForeignKey(Cart, on_delete=DO_NOTHING,null=True )

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile_photo(cls, id,family_email):
        return cls.objects.filter(id = id).update(family_email=family_email)

    
    @classmethod
    def search_username(cls,search_term):
        return cls.objects.filter(user__username__icontains = search_term)


    def get_absolute_url(self):
        return reverse('profile',args=[str(self.id)])


    def __str__(self) -> str:
       return self.user.username

class Category(models.Model):
    name = models.CharField(max_length = 80,blank=True)