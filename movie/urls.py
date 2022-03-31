from django.urls import path
from . import views
urlpatterns = [
    path('', views.MovieList , name='movie_list'),
    path('trends', views.trends , name='trends'),
    path('details/<int:pk>', views.MovieDetail_views , name='movie_detail'),
    path('search_results', views.search_results , name='search_results'),

    # Category
    path('trends', views.trends , name='trends'),

    path('recently', views.recently , name='recently'),

    path('top', views.top , name='top'),

    path('most', views.most , name='most'),

    path('action', views.action , name='action'),

    path('comedy', views.comedy , name='comedy'),

    path('adventure', views.adventure , name='adventure'),

    path('drama', views.drama , name='drama'),

    path('romance', views.romance , name='romance'),

    path('english', views.english , name='english'),

    path('arabic', views.arabic , name='arabic'),


    path('asian', views.asian , name='asian'),

    # Footer
    path('about', views.about , name='about'),


]