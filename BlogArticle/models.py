from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

################## class Category ##################
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)    
    thumbnail = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

################## class Article ##################
class Article(models.Model):
    STATUSE_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    category = models.ManyToManyField(Category, related_name="articles")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(auto_now=True)
    statuse = models.CharField(max_length=1, choices=STATUSE_CHOICES)

################## class Users ##################
class UserArticle(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('R', 'Rather not say'),
        ('C', 'Custom')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_number = models.CharField(max_length=10)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

############### class User ###############
class MyUserManager(BaseUserManager):

    def _create_user(self, email, user_name, mobile_number, password, **extra_fields):
        values = [email, user_name, mobile_number]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_name=user_name,
            mobile_number=mobile_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, user_name, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, user_name, mobile_number, password, **extra_fields)

    def create_superuser(self, email, user_name, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, user_name, mobile_number, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('R', 'Rather not say'),
        ('C', 'Custom')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'mobile_number']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name



