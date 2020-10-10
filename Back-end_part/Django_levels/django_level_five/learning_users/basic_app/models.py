from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional data
    portofolio_site = models.URLField(blank=True, null=True, max_length=200)
    
    profile_pic =models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return 
