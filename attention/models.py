from django.db import models
# Create your models here.
class Attention(models.Model):
    content = models.TextField()
    attention_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content