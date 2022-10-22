from audioop import reverse
from email import message
from multiprocessing import context
from multiprocessing.sharedctypes import Value
from unicodedata import category
# from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Category, SubscribedUser
from django.contrib.auth import get_user_model




def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUser.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUser()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
# About View
class HomePage(TemplateView):
    template_name = 'post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.order_by("-published_date")


    def get_context_data(self, *args, **kwargs):
        post = Post.objects.order_by("-published_date")        
        context = {'TopKey' : post, 'Postkey' : post}
        context['post'] = post
        return context





def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request,'category.html', {'cats':cats, 'category_post' : category_post})





# Post List View
class PostListView(ListView):
    model = Post
    

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data()
        context['cat_menu'] = cat_menu
        return context


# Post Details View
class PostDetailView(DetailView):
    model = Post



# Create New Post View
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

# Update Post View
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

# Drafts Post View
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# Delete Post View
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')



















#######################################
## Functions that require a pk match ##
#######################################

# Publish Post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)



# Approve Comment
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

# Remove Comment
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('post_list'))




# def filtered(request):
#     Post = Post.objects.all()
#     print(Post)
#     return render(request, )

# class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
#     """
#     Log out the user and display the 'You are logged out' message.
#     """
#     next_page = None
#     redirect_field_name = REDIRECT_FIELD_NAME
#     template_name = 'registration/logged_out.html'
#     extra_context = None

#     ...

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         current_site = get_current_site(self.request)
#         context.update({
#             'site': current_site,
#             'site_name': current_site.name,
#             'title': _('Logged out'),
#             **(self.extra_context or {})
#         })
#         return context


