from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from PIL import Image

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CITIES = (
        ('Wah', 'Wah'),('Taxila', 'Taxila'),('Kohat','Kohat'),('Vehari','Vehari'),
        ('Chakwal','Chakwal'),('Kalar Kahar','Kalar Kahar'), ('Sangla Hill','Sangla Hill'),
        ('Shah Kot','Shah Kot'),('Gojra','Gojra'),('Toba Tek Singh','Toba Tek Singh'),('Multan','Multan'),
        )
    COUNTRIES = (
        ('Pakistan','Pakistan'),('UK','UK'),('Eygpt', 'Eygpt')
    )
    INDUSTRIES = (
        ("Apparel & Fashion","Apparel & Fashion"),
	("Banking","Banking"),
	("Business Supplies & Equipment","Business Supplies & Equipment"),
	("Civic & Social Organization","Civic & Social Organization"),
	("Commercial Real Estate","Commercial Real Estate"),
	("Computer Software","Computer Software"),
	("Consumer Goods","Consumer Goods"),
	("Consumer Services","Consumer Services"),
	("Cosmetics","Cosmetics"),
	("Education","Education"),
	("Entertainment","Entertainment"),
	("Events Services","Events Services"),
	("Financial Services","Financial Services"),
	("Food & Beverage","Food & Beverage"),
	("Furniture","Furniture"),
	("Government Administration","Government Administration"),
	("Health, Wellness & Fitness","Health, Wellness & Fitness"),
	("Hospitality, Hotels","Hospitality, Hotels"),
	("Human Resources","Human Resources"),
	("Information Technology & Services","Information Technology & Services"),
	("Insurance","Insurance"),
	("Leisure & Travel","Leisure & Travel"),
	("Luxury Goods & Jewelry","Luxury Goods & Jewelry"),
	("Marketing & Advertising","Marketing & Advertising"),
	("Oil & Energy","Oil & Energy"),
	("Other","Other"),
	("Pharmaceuticals","Pharmaceuticals"),
	("Public Relations","Public Relations"),
	("Retail","Retail"),
	("Telecommunications","Telecommunications"),
	("Tobacco","Tobacco"),
    ("Utilities","Utilities"),

    )
  
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default ='default.jpg', upload_to ='profile_pics')
    email_confirmed = models.BooleanField(default=False)
    phone = models.CharField(_('phone'), max_length=100 ,unique=True, null=True)
    gender = models.CharField(max_length=100, null=True, choices=GENDER )
    city = models.CharField(max_length=500, null=True, choices=COUNTRIES )
    city = models.CharField(max_length=500, null=True, choices=CITIES )
    industry = models.CharField(max_length=500, null=True, choices=INDUSTRIES)
    job_role = models.CharField(max_length=500, null=True)
    comany_name = models.CharField(max_length=2000, null=True)
    company_email = models.EmailField(null=True,unique=True)




    def __str__(self):
        return f'{self.user.first_name} Profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
