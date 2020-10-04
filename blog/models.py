from django.db import models
from django.conf import settings
from django.utils import timezone
from gamersijuan.utils import unique_slug_generator
from django.urls import reverse
from django.db.models.signals import pre_save
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


User = settings.AUTH_USER_MODEL


def user_media_path(instance, filename):
    return 'user/{0}/images/{1}'.format(instance.author.id, filename)


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Date Published', default=timezone.now, blank=True) # noqa
    banner = models.ImageField('Post Banner', upload_to=user_media_path, null=True, blank=True) # noqa
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    tags = TaggableManager(blank=True)
    feature = models.BooleanField('Homepage feature?', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})


def pre_save_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post, sender=Post)


class Affiliate(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='affiliates') # noqa
    when = models.DateTimeField(default=timezone.now, blank=True)
    seller = models.CharField(max_length=250, blank=True)
    product_image = models.ImageField(upload_to=user_media_path, null=True, blank=True) # noqa
    url = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.post.title