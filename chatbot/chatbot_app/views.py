from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from .forms import ChatForm
from .models import ChatMessage
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.core.paginator import Page

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

            if request.user.is_authenticated:
                chat_message = ChatMessage(text=user_message, response=str(response),user = request.user)
                chat_message.save()
                print("chat saved")
            else:
                pass

            return JsonResponse({'response': str(response), 'message' : user_message})
    else:
        form = ChatForm()
    return render(request, 'chat.html', {'form': form})

def load_chats(request):
    if request.user.is_authenticated:
        user = request.user
        # Fetch unique dates and their count from ChatMessage
        dates_with_counts = ChatMessage.objects.filter(user=user).values('timestamp__date').annotate(count=Count('id')).order_by('timestamp__date')

        date_list = []
        for entry in dates_with_counts:
            date_list.append({
                'date': entry['timestamp__date'].strftime('%Y-%m-%d'),
                'count': entry['count']
            })

        return JsonResponse({'dates': date_list})
    else:
        return JsonResponse({'error': 'User not authenticated'})
    
def load_chat(request):
    if request.user.is_authenticated:
        user = request.user
        date = request.GET.get('date', '')  # Get the 'date' parameter from the request's query parameters

        chat_messages = ChatMessage.objects.filter(user=user, timestamp__date=date).order_by('timestamp')

        chat_list = []
        for entry in chat_messages:
            chat_list.append({
                'user': str(entry.text),
                'bot': str(entry.response)
            })
        
        return JsonResponse({'chat': chat_list})
    else:
        return JsonResponse({'error': 'User not authenticated'})

'''def paginate_by_date(queryset, items_per_page, target_date, date_pagination):
    """
    Custom date-based pagination function. It paginates queryset by date.
    :param queryset: QuerySet to paginate
    :param items_per_page: Number of items per page
    :param target_date: Target date for fetching the page
    :param date_pagination: Enable date-based pagination
    :return: Paginated Page object
    """
    if not date_pagination:
        # Fall back to standard pagination if date_pagination is disabled
        return Paginator(queryset, items_per_page).get_page(1)

    if target_date:
        # If a target date is provided, fetch the corresponding page
        page = 1
        for i, item in enumerate(queryset):
            if item.date_field.date() == target_date:
                page = (i // items_per_page) + 1
                break
        return Paginator(queryset, items_per_page).get_page(page)
    else:
        # If no target date is provided, return the first page
        return Paginator(queryset, items_per_page).get_page(1)'''

def home_screen_view(request):
    return render(request,"chat.html")