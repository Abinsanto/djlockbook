# from django.db import models
#
#
#
# class customer(models.Model):
#     title=models.CharField(max_length=100)
#     author=models.CharField(max_length=100)
#     short=models.CharField(max_length=100)


# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
#
# class Customer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     short = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f"{self.title} ({self.user.username})"



from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # links each record to a user
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    short = models.TextField()

    def __str__(self):
        return self.title
