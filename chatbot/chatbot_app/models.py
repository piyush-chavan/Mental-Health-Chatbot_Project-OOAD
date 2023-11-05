from django.db import models
from account.models import Account

class ChatMessage(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

