"""tester05 URL Configuration

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
from django.contrib import admin
from django.urls import path
from test_module.views import show_all_tests, passing_test, check_answer

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', show_all_tests, name='home-page'),
    path('test/<str:test_name>/', passing_test, name='test-page'),
    path('test/<str:test_name>/results', check_answer, name='result'),
]
