from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    introduction = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    minutes = models.IntegerField()
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.title
