"""
URL configuration for LostAndFound project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from user import views as user_view
from item import views as item_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_view.register_view, name='registration'),
    path('login/', user_view.login_view, name='login'),
    path('logout/', user_view.logout_view, name='logout'),
    path('create/', item_view.item_create, name='report_create'),
    path('home/', item_view.list_reports, name='dashboard'),
    path('detail/<int:pk>/', item_view.report_detail, name='report_detail'),
    path('update/<int:pk>/', item_view.report_update, name='report_update'),
    path('delete/<int:pk>/', item_view.report_delete, name='report_delete'),
    path('my-reports/', item_view.my_reports, name='my_reports'),
]
