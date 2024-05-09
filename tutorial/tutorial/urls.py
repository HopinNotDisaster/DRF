"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include, re_path
from quickstart import views as qv
from book import views as bv
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()
# router.register(r'users', qv.UserViewsets)
# router.register(r'groups', qv.GroupViewsets)
router.register(r'books', bv.BookViewsets)
router.register(r'categorys', bv.CategoryViewsets)


def compare_fun(req):
    # pass
    users = User.objects.all()

    users = [{'name': u.username, } for u in users]

    return JsonResponse({

        'code': 0,
        "msg": '获取用户列表成功',
        'datas': users

    })


@api_view(["GET"])
def api_root(req, format=None):
    return Response({
        "users": reverse('user-list', request=req, format=format),
        "groups": reverse('group-list', request=req, format=format),
        "books": reverse('book-list', request=req, format=format),
        "categorys": reverse('category-list', request=req, format=format),
    }, status=status.HTTP_200_OK)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('compare/', compare_fun),

    path('', include(router.urls)),

    path("", api_root, name='api-root'),

    re_path('^users/$', qv.UserListView.as_view(), name='user-list'),
    re_path('^users/(?P<id>[^/.]+)/$', qv.UserDetailView.as_view(), name='user-detail'),

    # re_path('^groups/$', qv.GroupListView.as_view(), name='group-list'),
    # re_path('^groups/(?P<id>[^/.]+)/$', qv.GroupDetailView.as_view(), name='group-detail'),

    re_path('^groups/$', qv.GroupListGenericView.as_view(), name='group-list'),
    re_path('^groups/(?P<id>[^/.]+)/$', qv.GroupDetailGenericView.as_view(), name='group-detail'),

    # re_path('^books/$', bv.book_list, name='book-list'),
    # re_path('^books/(?P<id>[^/.]+)/$', bv.book_detail, name='book-detail'),

    # re_path('^books/$', bv.BookListView.as_view(), name='book-list'),
    # re_path('^books/(?P<id>[^/.]+)/$', bv.BookDetailView.as_view(), name='book-detail'),

    # re_path('^books/$', bv.BookListCreateAPIView.as_view(), name='book-list'),
    # re_path('^books/(?P<id>[^/.]+)/$', bv.BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),

    # re_path('^categorys/$', bv.category_list, name='category-list'),
    # re_path('^categorys/(?P<id>[^/.]+)/$', bv.category_detail, name='category-detail'),

    # re_path('^categorys/$', bv.CategoryListView.as_view(), name='category-list'),
    # re_path('^categorys/(?P<id>[^/.]+)/$', bv.CategoryDetailView.as_view(), name='category-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
