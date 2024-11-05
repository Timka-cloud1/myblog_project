"""
URL configuration for myblog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from blog import views
from blog.views import PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', PostListView.as_view(), name='post_list'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),


    path('posts/cbv/', PostListView.as_view(), name='post_list_cbv'),
    path('post/cbv/<int:pk>/', PostDetailView.as_view(), name='post_detail_cbv'),
    # path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
