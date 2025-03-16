from django.db import models
# Create your models here.


newsLetterOption = [('W', 'WEEKLY'), ('M', 'MONTHLY')]


class Subscribe(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailId = models.EmailField(max_length=50)
    option = models.CharField(
        max_length=2, choices=newsLetterOption, default='M')
