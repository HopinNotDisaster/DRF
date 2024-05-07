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
from django.urls import path, include
from quickstart import views as qv
from book import views as bv
from django.contrib.auth.models import User
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', qv.UserViewsets)
router.register(r'groups', qv.GroupViewsets)


# router.register(r'books', bv.BookViewsets)


def compare_fun(req):
    # pass
    users = User.objects.all()

    users = [{'name': u.username, } for u in users]

    return JsonResponse({

        'code': 0,
        "msg": '获取用户列表成功',
        'datas': users

    })


urlpatterns = [
    path('admin/', admin.site.urls),

    path('compare/', compare_fun),

    path('', include(router.urls)),

    path('books/', bv.book_list, name='book-list'),
    path('books/<int:id>/', bv.book_detail, name='book-detail'),

    path('categorys/', bv.category_list, name='category-list'),
    path('categorys/<int:id>/', bv.category_detail, name='category-detail'),
]
