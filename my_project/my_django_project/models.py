from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, role, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(
                email = email,
                name = name,
                role = role
              )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name, role, password=None):
        user = self.create_user(
            email=email,
            name= name,
            role= role, 
            password= password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']
    
    def __str__(self):
        return self.name   
    
    def has_perm(self, perm, obj = None):
        return self.is_superuser or self.is_staff
    
    def has_module_perms(self, app_label):
        return self.is_superuser or self.is_staff