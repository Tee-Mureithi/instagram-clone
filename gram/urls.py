from django.urls import path,include
from gram.views import PostLikeToggle, PostLikeAPIToggle
from . import views

app_name = "gram"   


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    
    path("register", views.register_request, name="register"),
    path('account/', include('django.contrib.auth.urls')),
    path("login", views.login_request, name="login"),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('post/<id>', views.post_comment, name='comment'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    path('like', views.like_post, name='like_post'),
    path('search/', views.search_profile, name='search'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow')
]