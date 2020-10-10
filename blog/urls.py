from django.urls import path
from . import views
from blog.views import HomeViewList, PostDetailView, NewsViewList, ReviewsViewList, HardwareViewList, SearchResultsView

app_name = 'blog'


urlpatterns = [
    path('', HomeViewList.as_view(), name='home'),
    path('news/', NewsViewList.as_view(), name='news'),
    path('reviews/', ReviewsViewList.as_view(), name='reviews'),
    path('hardware/', HardwareViewList.as_view(), name='hardware'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    
    
]