"""django_todo URL Configuration

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
from django.contrib import admin
from django.urls import path
# This will allow us to use the say_hello function inside the urls file
from todo.views import get_todo_list, add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    # Define a url thats going to trigger the function and return the http response to the browser
    # To do that we use the built in path function which takes three arguments
    # - the url that the user is going to type in,
    # - the view function that it's going to return
    # - name parameter
    path("", get_todo_list, name='get_todo_list'),
    path("add", add_item, name='add')
]
