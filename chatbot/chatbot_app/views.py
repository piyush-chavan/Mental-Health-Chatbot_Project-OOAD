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
import csv

chatbot = ChatBot('MyBot')
custom_trainer = ListTrainer(chatbot)

def trainFromDataset():
    for x in range(1,9):
        with open("static/training_data/" + str(x) + ".csv",mode = 'r',encoding='utf-8') as dataset:

            reader = csv.reader(dataset)

            for row in reader:

                custom_trainer.train(row)

    return

# trainFromDataset()

def chat_response(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            response = chatbot.get_response(user_message)

            if request.user.is_authenticated:
                chat_message = ChatMessage(text=user_message, response=str(response),user = request.user)
                chat_message.save()
                print("chat saved")
            

            return JsonResponse({'response': str(response), 'message' : user_message})
    return

def chat_view(request):
    
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
    
def load_survey(request):

    GAD7 = ["Feeling nervous, anxious, or on edge",
            "Not being able to stop or control worrying",
            "Worrying too much about different things",
            "Trouble relaxing",
            "Being so restless that it is hard to sit still",
            "Becoming easily annoyed or irritable",
            "Feeling afraid, as if something awful might happen"
            ]
    GAD7_labels = ["Not at all","Several days","More than half the days","Nearly every day"]
    
    PHQ9 = ["Little interest or pleasure in doing things?",
            "Feeling down, depressed, or hopeless?",
            "Trouble falling or staying asleep, or sleeping too much?",
            "Feeling tired or having little energy?",
            "Poor appetite or overeating?",
            "Feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
            "Trouble concentrating on things, such as reading the newspaper or watching television?",
            "Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?",
            "Thoughts that you would be better off dead, or of hurting yourself in some way?"
            ]
    
    stress = [
        "In the last month, how often have you been upset because of something that happened unexpectedly?",
        " In the last month, how often have you felt that you were unable to control the important things in your life?",
        "In the last month, how often have you felt nervous and stressed?",
        "In the last month, how often have you felt confident about your ability to handle your personal problems?",
        "In the last month, how often have you felt that things were going your way?",
        "In the last month, how often have you found that you could not cope with all the things that you had to do?",
        "In the last month, how often have you been able to control irritations in your life?",
        "In the last month, how often have you felt that you were on top of things?",
        "In the last month, how often have you been angered because of things that happened that were outside of your control?",
        "In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?"
    ]
    
    stress_labels = ["Never","Almost never","Sometimes","Fairly often","Very often"]
    ptsd = [
        "Repeated, disturbing memories,thoughts, or images of a stressfulexperience from the past",
        "Repeated disturbing dreams of a stressful experience from the past",
        "Suddenly acting or feeling as if a stressfull experience were happening again (as if you were reliving it)",
        "Feeling very upset when something reminded you of a stressful experience from the past",
        "Having physical reactions (e.g., heart pounding, trouble breathing, sweating) when something reminded you of a stressful experience from the past",
        "Avoiding thinking about or talking about a stressful experience from the past or avoiding having feelings related to it",
        "Avoiding activities or situations because they reminded you of a stressful experience from the past",
        "Trouble remembering important parts of a stressful experience from the past",
        "Loss of interest in activities that you used to enjoy",
        "Feeling distant or cut off from other people",
        "Feeling emotionally numb or being unable to have loving feelings for those close to you",
        "Feeling as if your future will somehow be cut short",
        "Trouble falling or staying asleep",
        "Feeling irritable or having angry outbursts",
        "Having difficulty concentrating",
        "Being “super‐alert” or watchful or on guard",
        "Feeling jumpy or easily startled"
    ]
    ptsd_labels = ["Not at all", "A little bit", "Moderately", "Quite a bit", "Extremely"]
    addiction = []
    bipolar = []
    eating = []
    schizophrenia = []

    return JsonResponse({'anxiety' : GAD7, 'depression' : PHQ9 , 'stress' : stress, 'ptsd':ptsd,'addiction':addiction,'bipolar':bipolar,'eating':eating,'schizophrenia':schizophrenia,
                         'anxiety_labels': GAD7_labels, 'depression_labels':GAD7_labels, 'stress_labels':stress_labels, 'ptsd_labels':ptsd_labels})
    
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

def landing(request):
    return render(request,"landing.html")