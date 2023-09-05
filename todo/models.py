from django.db import models

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)   #ForeignKey 사용할 땐, 꼭 on_delete 있어야 함. 유저가 없어질 때 어떻게 할 거냐?
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.content