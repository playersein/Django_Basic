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
    
class Comment(models.Model):    # user 하나가 여러 개 comment, todo 하나가 여러 개 comment -> 일대다
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)   # user.User -> import를 위핸
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)    # relate_name 을 학습해서 써서 사용해보기
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)