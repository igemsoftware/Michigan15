from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser)

class UserRegistration(models.Model):
    email = models.EmailField(blank=False)
    user_name = models.CharField(max_length=50, default='YourName', blank=False)
    password = models.CharField(max_length=120, default='password123', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)

class UserAuthentication(models.Model):
    user_name = models.CharField(max_length=50, default='YourUserName')
    password = models.CharField(max_length=120, default='password123', blank=False)

    def __str__(self):
        return (self.user_name + ', ' + self.email)

# Begins Greg's work
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        creates and saves a User with the given email and password
        """
        if not email:raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        creates and saves a superusesr with the given email and password
        """
        user = self.create_user(email, password = password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email adress',
        max_length=255,
        unique=True,
        )
    is_active = models.BooleanField(default= True)
    is_admin = models.BooleanField(default= False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        #The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        #Simplest possible answer: Yes, always
        return True

    @property

    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: Yes, always
        return self.is_admin
    
# Ends Greg's work

# class Protocol(models.Model):
#     title = models.TextField()
#     # author = ... TODO: tie in with user permissions etc.
#     date_of_upload = models.DateField
#     protocol_type = models.CharField(max_length=2, choices=PROTOCOL_TYPES, null=True)
#     rating = models.DecimalField(
#         validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
#         max_digits=3, decimal_places=2, default = 0.00)
#     protocol = models.TextField(default = '')
