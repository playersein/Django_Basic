from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile = models.TextField(null=True, blank=True)
    like_todos = models.ManyToManyField("todo.Todo", related_name="like_users") # foreign key가 아니라 manytomanyfield
    # manytomany -> 가운데 bridge table이 생긴다
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")    # symmetrical=True : 싸이 일촌맺기처럼 쌍방향 동시에.. False: 한 사람만 일방적으로 팔로우 하는 거