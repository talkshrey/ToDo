from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='')

    def __str__(self):
        return self.email


# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # due_date = models.DateTimeField()
    compulsory = models.BooleanField()
    priority_order = models.IntegerField(default=0)

    # add foreign key

    def __str__(self):
        return self.title
