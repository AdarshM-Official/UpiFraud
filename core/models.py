from django.db import models
from django.contrib.auth.models import User # what is this for? This is for importing the built-in User model provided by Django's authentication system. The User model is used to represent users in the application, and it includes fields such as username, password, email, and more. By importing this model, you can create relationships between your custom models and the User model, allowing you to associate data with specific users in your application.

# Create your models here.

class user(User):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)