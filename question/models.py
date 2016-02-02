from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

# model question
class Question(models.Model):
    title = models.CharField(max_length=255) # title Question
    descipition = models.CharField(max_length=400)
    author=models.ForeignKey(settings.AUTH_USER_MODEL)

		

