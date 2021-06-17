"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from market import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.nav_category, name='nav_category'),
    path('pagination/', views.pageination, name='pageination'),
    path('about/', views.about, name='about'),
    path('product/<str:pk>/', views.category, name='category'),
    path('product/', views.all, name='allcategory'),
    path('product/category/<str:pk>', views.product_detail_2, name='detail'),
    path('contact/', views.contact_view, name='contact'),
    # path('product/category/<str:pk>/', views.product_detail, name='detail'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
