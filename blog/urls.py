from django.urls import path
from . import views
from blog.views import HomeViewList

app_name = 'school'


urlpatterns = [
    path('', HomeViewList.as_view(), name='home'),
]