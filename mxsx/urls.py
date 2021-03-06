"""mxsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.views.static import serve
from mxsx.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

# from goods.views import GoodsListView

router = DefaultRouter()

#配置goods的url
router.register(r'goods',GoodsListViewSet)
# 配置Category的url
router.register(r'categorys', CategoryViewSet)

urlpatterns = [
    re_path('^', include(router.urls)),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('docs', include_docs_urls(title='mxsx')),
    path('api-auth', include('rest_framework.urls')),
    # path('goods', GoodsListView.as_view(),name='goods-list'),
    # 文件
    path('media/<path:path>', serve, {'document_root':MEDIA_ROOT}),
    path('api-token-auth/',views.obtain_auth_token),
    # jwt的token认证接口
]
