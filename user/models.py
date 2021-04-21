from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class School(models.Model):
    school_code = models.CharField(max_length=20, null=False)
    school_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.school_name


class UserManager(BaseUserManager):
    def create_user(self, username, password, nickname=None):
        if not username:
            raise ValueError(_('Users must have an username'))
        user = self.model(username=username,
                          password=password,
                          nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, nickname):
        user = self.create_user(username, password, nickname)
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    GENDER_CHOICES = (("F", "FEMALE"), ("M", "Male"), ("E", "ETC"))

    username = models.CharField(max_length=30, null=False, unique=True)
    nickname = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=14, null=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              null=False,
                              default="M")
    birthday = models.DateField(null=True)
    student_id = models.CharField(max_length=8, null=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined', )

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.is_superuser