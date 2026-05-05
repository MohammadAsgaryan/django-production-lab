from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
# Create your views here.

# Function Base View show a template
'''
def indexView(request):
    """
    a function based view to show index page
    """
    name = "mmd"
    context = {"name": name}
    return render(request, "index.html", context)
'''
class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "mmd"
        context["posts"] = Post.objects.all()
        return context
    
    ''' FBV for redirect
from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.com')
'''

class RedirectToMaktab(RedirectView):
    """
    Redirection view sample for maktabkhooneh
    """
    url = 'https://maktabkhooneh.com'
    
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    
    
class PostListView(ListView):
    """
    A class based view to show list of posts
    """
    queryset = Post.objects.all()
    # model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = '-id'
    
    
class PostDetailView(DetailView):
    """
    A class based view to show details of a post
    """
    model = Post
    