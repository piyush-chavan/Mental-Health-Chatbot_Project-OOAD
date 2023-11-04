from django.shortcuts import render
from main.forms import ChatForm
from main.models import ChatMessage
from chatterbot import ChatBot

chatbot = ChatBot('MyBot')      

def chat_view(request):
    if request.POST :
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            response = chatbot.get_response(user_message)

            # Save the conversation in the database
            chat_message = ChatMessage(text=user_message, response=str(response))
            chat_message.save()

            return render(request, 'chat.html', {'form': form, 'response': response})
    else:
        form = ChatForm()

    return render(request, 'chat.html', {'form': form})

def home_screen_view(request):
    return render(request,"chat.html")
