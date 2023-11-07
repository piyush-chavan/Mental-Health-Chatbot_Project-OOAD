from django.db import models
from account.models import Account

class ChatMessage(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField(default = None)
    response = models.TextField(default = None)
    timestamp = models.DateTimeField(auto_now_add=True)

