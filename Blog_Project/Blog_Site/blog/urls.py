from unicodedata import name
from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from .views import CategoryView

urlpatterns = [
    # path('home/', views.HomePage.as_view(),name='home'),

    path('', views.HomePage.as_view(), name='home'),



    path('subscribe', views.subscribe, name='subscribe'),




     path('category/<str:cats>/', CategoryView, name= 'category'),
    path('/blogs', views.PostListView.as_view(), name='post_list'),
    path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/(?P<pk>\d+)/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/(?P<pk>\d+)/remove/',
         views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),

    path('comment/(?P<pk>\d+)/approve/',
         views.comment_approve, name='comment_approve'),
    path('comment/(?P<pk>\d+)/remove/',
         views.comment_remove, name='comment_remove'),
    path('post/(?P<pk>\d+)/publish/', views.post_publish, name='post_publish'),
    path('logout/', views.logout, name='logout'),
    # path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
