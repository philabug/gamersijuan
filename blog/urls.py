from django.urls import path
from . import views
from blog.views import HomeViewList, PostDetailView, NewsViewList, ReviewsViewList, HardwareViewList, SearchResultsView, \
    GamesViewList, GuideViewList

app_name = 'blog'


urlpatterns = [
    path('', HomeViewList.as_view(), name='home'),
    path('news/', NewsViewList.as_view(), name='news'),
    path('reviews/', ReviewsViewList.as_view(), name='reviews'),
    path('hardware/', HardwareViewList.as_view(), name='hardware'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('games/', GamesViewList.as_view(), name='games'),
    path('guide/', GuideViewList.as_view(), name='guide'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    
    
]