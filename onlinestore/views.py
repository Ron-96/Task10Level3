from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView


# Create your views here.


def store(request):
    """
    View function for handling album title suggestions submitted via a form.

    This view function handles both GET and POST requests. When a GET request is made,
    it initializes an empty AlbumTitleSuggestionForm to display the suggestion form.
    When a POST request is made, it validates the form data and saves the valid
    suggestion to the database.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: If the request method is POST and the form data is valid, it redirects
              the user to the 'suggestion_list' view. Otherwise, it renders the 'WebTest.html'
              template with the AlbumTitleSuggestionForm to display the suggestion form.
    :rtype: HttpResponse

    :note: This view expects a template named 'WebTest.html' that includes the form for submitting
           album title suggestions. The form should be linked to this view's URL path.
    """

    if request.method == 'POST':
        form = AlbumTitleSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alex:suggestion_list')
    else:
        form = AlbumTitleSuggestionForm()
    return render(request, 'WebTest.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def noplant(request):
    """
    View function to render the 'noplant.html' template.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'noplant.html' template.
    :rtype: HttpResponse
    """
    return render(request, 'noplant.html')

def typical(request):
    """
    View function to render the 'typical.html' template.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'typical.html' template.
    :rtype: HttpResponse
    """
    return render(request, 'typical.html')

def exgirl(request):
    """
    View function to render the 'exgirl.html' template.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'exgirl.html' template.
    :rtype: HttpResponse
    """
    return render(request, 'exgirl.html')

def evil(request):
    """
    View function to render the 'evil.html' template.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'evil.html' template.
    :rtype: HttpResponse
    """
    return render(request, 'evil.html')

def blah(request):
    """
    View function to render the 'blah.html' template.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'blah.html' template.
    :rtype: HttpResponse
    """
    return render(request, 'blah.html')

def user_login(request):
    """
    View function to render the 'login.html' template.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'login.html' template.
    :rtype: HttpResponse
    """
    return render(request, 'login.html')

def authenticate_user(request):
    """
    View function for authenticating user login.

    This view function handles POST requests containing user login credentials.
    It attempts to authenticate the user using the 'authenticate' method provided by Django.
    If the authentication is successful, the user is logged in, and the view redirects
    them to the 'WebTest' view. If the authentication fails, the user is redirected back
    to the 'login' view.

    :param request: The HTTP request object representing the user's login request.
    :type request: HttpRequest

    :returns: If the authentication is successful, it redirects the user to
              the 'WebTest' view. If the authentication fails, it redirects the user to the 'login' view.
    :rtype: HttpResponseRedirect

    :note: Make sure you have a login page with the name 'login' and a view 'WebTest' to handle authenticated users.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('alex:login'))
    else:
        login(request, user)
    return HttpResponseRedirect(reverse('alex:WebTest')
)




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """
    View function for user registration.

    This view function handles both GET and POST requests for user registration.
    When a GET request is made, it initializes an empty UserCreationForm to display the registration form.
    When a POST request is made, it validates the form data and creates a new user account.

    :param request: The HTTP request object representing the user's registration request.
    :type request: HttpRequest

    :returns: If the request method is POST and the form data is valid, it redirects
              the user to the 'login' view to log in. Otherwise, it renders the 'register.html'
              template with the UserCreationForm to display the registration form.
    :rtype: HttpResponse

    :note: This view expects a template named 'register.html' that includes the form for user registration.
           The form should be linked to this view's URL path.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('alex:login'))  # Assuming you have a login page with the name 'login'
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumTitleSuggestionForm
from .models import AlbumTitleSuggestion



def suggestion_list(request):
    """
    View function to display a list of album title suggestions.

    This view function retrieves all the album title suggestions from the database
    using the AlbumTitleSuggestion model and passes them to the 'suggestion_list.html'
    template for rendering.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'suggestion_list.html' template, including the
              list of album title suggestions in the context.
    :rtype: HttpResponse
    """
    suggestions = AlbumTitleSuggestion.objects.all()
    return render(request, 'suggestion_list.html', {'suggestions': suggestions})

def vote(request, suggestion_id):
    """
    View function to handle voting for an album title suggestion.

    This view function increments the vote count for a specific album title suggestion
    identified by 'suggestion_id'. If the suggestion is found, its vote count is increased
    by 1, and the suggestion is saved to the database. After that, the user is redirected
    back to the 'suggestion_list' view.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :param suggestion_id: The primary key (ID) of the album title suggestion to vote for.
    :type suggestion_id: int

    :returns: An HTTP redirect response to the 'suggestion_list' view.
    :rtype: HttpResponseRedirect
    """
    suggestion = get_object_or_404(AlbumTitleSuggestion, pk=suggestion_id)
    suggestion.votes += 1
    suggestion.save()
    return redirect('alex:suggestion_list')

def blog(request):
    """
    View function to display a list of blog posts.

    This view function retrieves all the blog posts from the database using the Post
    model and orders them by the 'date' field in descending order. The sorted posts
    are then passed to the 'blog.html' template for rendering.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :returns: An HTTP response with the 'blog.html' template, including the list of blog
              posts in the context.
    :rtype: HttpResponse
    """
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog.html', {'posts': posts})

def post(request, pk):
    """
    View function to display a single blog post.

    This view function retrieves a specific blog post identified by its primary key (ID)
    'pk' from the database using the Post model. If the post is found, it is passed to
    the 'post.html' template for rendering.

    :param request: The HTTP request object representing the user's request.
    :type request: HttpRequest

    :param pk: The primary key (ID) of the blog post to display.
    :type pk: int

    :returns: An HTTP response with the 'post.html' template, including the blog post
              in the context.
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})
