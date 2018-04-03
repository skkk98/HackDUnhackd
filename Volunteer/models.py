from django.db import models
from django.contrib.auth.models import User
from Ngo.models import Event

class Regevent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.CharField(max_length=1000)

class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    review = models.TextField(max_length = 250)
