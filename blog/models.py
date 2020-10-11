from django.db import models
from django.conf import settings
from django.utils import timezone
from gamersijuan.utils import unique_slug_generator
from django.urls import reverse
from django.db.models.signals import pre_save
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from meta.models import ModelMeta


User = settings.AUTH_USER_MODEL


def post_media_path(instance, filename):
    return 'post/{0}/{1}'.format(instance.slug, filename)


class Post(ModelMeta, models.Model):

    MAIN_CAT = (
        ('1', 'GAMES'),
        ('2', 'HARDWARE'),
        ('3', 'SERVICES'),
    )

    SUB_CAT = (
        ('1', 'NEWS'),
        ('2', 'REVIEWS'),
        ('3', 'GUIDE'),
    )
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    pub_date = models.DateTimeField('Date Published', default=timezone.now, blank=True) # noqa
    banner = models.ImageField('Post Banner', upload_to=post_media_path, null=True, blank=True) # noqa
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    tags = TaggableManager(blank=True)
    feature = models.BooleanField('Homepage feature', default=False)
    category = models.CharField(max_length=20, choices = MAIN_CAT)
    sub_category = models.CharField(max_length=20, choices = SUB_CAT, null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    deactivate = models.BooleanField(default=False)

    _metadata = {
        'title': 'title',
        'description': 'short_description',
    }

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
    seller = models.CharField(max_length=250, null=True, blank=True)
    product_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    product_image = models.ImageField(upload_to=post_media_path, null=True, blank=True) # noqa
    url = models.CharField(max_length=250, blank=True)
    

    def __str__(self):
        return self.post.title