from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatForm
from .models import ChatMessage
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('MyBot')
custom_trainer = ListTrainer(chatbot)

# Train your chatbot with custom data
custom_trainer.train([
    "What's your name?",
    "My name is MyBot.",
    "How are you?",
    "I'm just a machine, so I don't have feelings, but I'm here to help you."
])

def chat_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            response = chatbot.get_response(user_message)

            # Save the conversation in the database
            chat_message = ChatMessage(text=user_message, response=str(response))
            chat_message.save()

            return JsonResponse({'response': str(response), 'message' : user_message})
    else:
        form = ChatForm()
    return render(request, 'chat.html', {'form': form})

def home_screen_view(request):
    return render(request,"chat.html")