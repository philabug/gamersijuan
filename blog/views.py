from django.views.generic import ListView, DetailView, TemplateView, View, CreateView # noqa
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse # noqa
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.conf import settings


class HomeViewList(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeViewList, self).get_context_data(*args, **kwargs)
        context['features'] = Post.objects.filter(feature=True).order_by('-id')
        context['posts'] = Post.objects.all().order_by('-id')
        return context