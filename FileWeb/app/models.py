from django.db import models
from datetime import datetime


class Field(models.Model):
    charField = models.CharField(max_length=1000)
    fileField = models.FileField(upload_to='files')


def before_update_field(sender, **kwargs):
    notifier('old ')


def after_update_field(sender, **kwargs):
    notifier('new ')


def notifier(string):
    with open('log.txt', 'a') as f:
        f.write(string)
        f.write(str(datetime.now()) + ' ')
        f.close()
