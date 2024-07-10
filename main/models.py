from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class User(AbstractUser):
#     img = models.ImageField(upload_to='img', blank=True, null=True)
#     bio = models.TextField(max_length=500, blank=True, null=True)
#     location = models.CharField(max_length=50, blank=True, null=True)
#     birth_date = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=50, blank=True, null=True)
#     country = models.CharField(max_length=50, blank=True, null=True)
#     phone = models.CharField(max_length=50, blank=True, null=True)

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def last_img(self):
        return BlogImg.objects.filter(blog__id = self.id).last().img


class BlogImg(models.Model):
    img = models.ImageField(upload_to='blog-img/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

class BlogVideo(models.Model):
    video = models.FileField(upload_to='blog-vidos/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} -> {self.blog.title}"
    

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email address')
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
