from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import csv

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

'''trainer = ListTrainer(bot)

with open("C:/Users/Hitesh Dhiman/OneDrive/Desktop/Chatbot/datasets/4.csv",mode = 'r',encoding='utf-8') as dataset:

    reader = csv.reader(dataset)

    for row in reader:

        trainer.train(row)
'''
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
