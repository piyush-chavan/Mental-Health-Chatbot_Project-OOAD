from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_response, name='chat_view'),
    path('load_chats/', views.load_chats, name='load_chats'),
    path('load_chat/', views.load_chat, name='load_chat'),
    path('load_survey/', views.load_survey, name='load_survey'),
   
]
