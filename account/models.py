import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='avatar/', default='avatar/me.png') # noqa
    entry_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_description = models.TextField('Short Description', null=True, blank=True) # noqa
    location = models.CharField('Location', max_length=250, null=True, blank=True) # noqaz
    skills = models.CharField('Skills', max_length=250, null=True, blank=True) # noqa
    cp_number = models.CharField('Cell Phone Number', max_length=20, null=True, blank=True ) # noqa

    def __str__(self):
        return self.user.username


class Links(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook = models.URLField('Facebook profile URL',max_length=200, null=True, blank=True) # noqa
    instagram = models.URLField('Instagram profile URL',max_length=200, null=True, blank=True) # noqa
    twitter = models.URLField('Twitter profile URL',max_length=200, null=True, blank=True) # noqa
    youtube = models.URLField('Youtube URL',max_length=200, null=True, blank=True) # noqa
    github = models.URLField('Github profile URL',max_length=200, null=True, blank=True) # noqa


class Privacy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    delete_account = models.BooleanField(default=False)
    deactivate_account = models.BooleanField(default=False)
