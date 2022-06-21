from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

LOCATION_CHOICES = (
    ('Nairobi','Nairobi'),
    ('Kisumu','Mombasa'),
    ('Mombasa','Mombasa'),
)

NEIGHBORHOOD_CHOICES = (
    ('Juja', 'Juja'),
    ('Kinoo','Kinoo'),
    ('Eastleigh','Eastleigh'),
    ('Zimmerman','Zimmerman'),
    ('Ruiru','Ruiru'),
    ('Donholm','Donholm'),
)

class Neighborhood(models.Model):
    name = models.CharField(max_length=50,choices=NEIGHBORHOOD_CHOICES)
    location = models.CharField(max_length=70,choices=LOCATION_CHOICES)
    
    def create_neighborhood(self):
        self.save()
        
    def delete_neighborhodd(self):
        self.delete()
        
    def find_neighborhood(self, id):
        return Neighborhood.objects.get(id=id)
    
    def update_neighborhood(self):
        self.save()
    
    
    def __str__(self):
        return f"{self.location}/{self.name}"
    
class Profile(models.Model):
    image = CloudinaryField('image', null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Business(models.Model):
    image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def create_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
    
    def find_businesss(self,id):
        return Business.objects.get(id=id)
    
    def update_business(self):
        self.save()
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.name} {self.neighborhood.name}"

        
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    content = models.TextField(blank=True, null=True)
    profile_photo = CloudinaryField("image",blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return f'{self.title} Post'
    def delete_post(self):
        self.delete()
    def create_post(self):
        self.save()
    def update_post(self):
        self.update()

# Create your models here.
