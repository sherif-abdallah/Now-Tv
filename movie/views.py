from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator
import langid


def Reverse(lst):
    return [ele for ele in reversed(lst)]


def search_results(request):
    if request.method == "POST":
        search = request.POST['search']

        searched_movies = Movie.objects.filter(title__icontains=search)       

        return render(request, 'movie/search.html', {'search':search, 'searched_movies':searched_movies})
    else:
        return render(request, 'movie/search.html', {})


def MovieList(request):
        
        model = Movie.objects.all()

        return render(request, 'movie/movie_list.html', {'movie':model, 'p':model})




def trends(request):
        p = Movie.objects.filter(status='TRENDS')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/trends.html', {'movie':movies})

def recently(request):
        p = Movie.objects.filter(status='RECENTLY ADDED')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/recently.html', {'movie':movies})

def most(request):
        p = Movie.objects.filter(status='MOST WATCHED')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/most.html', {'movie':movies})



def top(request):
        p = Movie.objects.filter(status='TOP RATED')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/top.html', {'movie':movies})

def action(request):
        p = Movie.objects.filter(category='ACTION')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/action.html', {'movie':movies})

def comedy(request):
        p = Movie.objects.filter(category='COMEDY')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/comedy.html', {'movie':movies})

def adventure(request):
        p = Movie.objects.filter(category='ADVENTURE')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/adventure.html', {'movie':movies})


def drama(request):
        p = Movie.objects.filter(category='DRAMA')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/drama.html', {'movie':movies})


def romance(request):
        p = Movie.objects.filter(category='ROMANCE')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/romance.html', {'movie':movies})

def english(request):
        p = Movie.objects.filter(language='ENGLISH')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/english.html', {'movie':movies})


def arabic(request):
        p = Movie.objects.filter(language='ARABIC')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/arabic.html', {'movie':movies})




def asian(request):
        p = Movie.objects.filter(language='Asian')
        p = Reverse(p)
        p = Paginator(p , 8)
        page = request.GET.get('page')
        movies = p.get_page(page)
        return render(request, 'movie/asian.html', {'movie':movies})



# Footer
def about(request):
        return render(request, 'movie/aboutus.html')





def MovieDetail_views(request, pk):
        movie = Movie.objects.get(id=pk)
        create_view = Movie.objects.get(id=pk)
        create_view.blog_view += 1
        create_view.save()


        descripton_language = Movie.objects.get(id=pk).description
        descripton_language = langid.classify(descripton_language)[0]


        context = {
                'movie':movie,
                'descripton_language':descripton_language,
        }
        return render(request, 'movie/movie_detail.html', context)
