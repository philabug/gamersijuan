from django.views.generic import ListView, DetailView, TemplateView, View, CreateView # noqa
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse # noqa
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.conf import settings
from hitcount.views import HitCountDetailView


class HomeViewList(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeViewList, self).get_context_data(*args, **kwargs)
        context['features'] = Post.objects.filter(feature=True).order_by('-id')
        context['posts'] = Post.objects.all().order_by('-id')
        context['hardwares'] = Post.objects.filter(category='2').order_by('-id')
        return context


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    slug_field = 'slug'
    count_hit = True
    
 
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


class NewsViewList(ListView):
    queryset = Post.objects.filter(sub_category='1').order_by('-id')
    template_name = 'news.html'
    context_object_name = 'post_news'


class ReviewsViewList(ListView):
    queryset = Post.objects.filter(sub_category='2').order_by('-id')
    template_name = 'reviews.html'
    context_object_name = 'post_reviews'


class HardwareViewList(ListView):
    queryset = Post.objects.filter(category='2').order_by('-id')
    template_name = 'hardware.html'
    context_object_name = 'post_hardware'