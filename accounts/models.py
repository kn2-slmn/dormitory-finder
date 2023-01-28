from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STUDENT = 'STUDENT', 'Student'
        OWNER = 'OWNER', 'Owner'

    #! Middle name and birthdate must be required

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default='Middle')
    email_address = models.EmailField(unique=True)
    birthdate = models.DateField(
        # auto_now=False, auto_now_add=False, 
        default=timezone.now
    )
    type = models.CharField(default=Types.ADMIN, choices=Types.choices, max_length=8)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = [first_name, last_name]

    objects = UserManager()

    def __str__(self):
        return self.email_address

class OwnerProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    messenger_link = models.CharField(max_length=50)

class StudentProfile(models.Model):
    class Colleges(models.TextChoices):
        CAFSD = 'CAFSD', 'Cafsd'
        CAS = 'CAS', 'Cas'
        CBEA = 'CBEA', 'Cbea'
        CHS = 'CHS', 'Chs'
        COE = 'COE', 'Coe'

    account = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=10)
    college = models.CharField(choices=Colleges.choices, max_length=10)
    
    # ! Implement when dormitory table is created 
    # current_dorm = models.OneToOneField()

# Manager classes for Proxy
class AdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)

class OwnerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.OWNER)

class StudentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)


# Proxy classes 
class Admin(User):
    admins = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN
        return super(Admin, self).save(*args, **kwargs)

class Owner(User):
    owners = OwnerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.OWNER
        return super(Owner, self).save(*args, **kwargs)

class Student(User):
    students = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super(Student, self).save(*args, **kwargs)