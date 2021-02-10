"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from generator import views
#first arguement of path is routing string and second is view you wanna return
urlpatterns = [
    path('',views.home,name='home'),
    path('password/',views.password,name='password'),#referencing name as password as thet do not need to be same thing
    path('about/',views.about,name='about'),
]
#it deals with what to do with the url string that we provide in the browser,everything starts from here,anything somone types in browser url comes here