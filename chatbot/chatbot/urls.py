"""chatbot URL Configuration

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
from django.conf.urls import url


from chatbot_app.views import(
    home_screen_view,
    chat_view,
    load_chats,
    load_chat,
    load_survey,
    landing,
    chat_response,
    about,
    content,
    save_survey
)

from account.views import(
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_screen_view, name = "home"),
    path('register/',registration_view,name="register"),
    path('logout/',logout_view,name="logout"),
    path('login/', login_view, name="login"),
    path('chat/', chat_view, name='chat_view'),
    path('chat_data/', chat_response, name='chat_response'),
    path('load_chats/', load_chats, name='load_chats'),
    path('load_chat/', load_chat, name='load_chat'),
    path('', landing, name='landing_page'),
    path('load_survey/', load_survey, name='load_survey'),
    path('about/',about, name='about'),
    path('content/',content, name='content'),
    path('save_survey/',save_survey, name='save_survey'),
]
