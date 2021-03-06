"""whiteSpace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, include
from products.views import MainView, NavView

urlpatterns = [
    path('users' ,include('users.urls')),
    path('cart', include('orders.urls')),
    path('orders', include('orders.urls')),
    path('products', include('reviews.urls')),
    path('products', include('products.urls')),
    path('nav', NavView.as_view()),
    path('main', MainView.as_view()),
]
