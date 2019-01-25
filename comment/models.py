from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="comments")

    root = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name='root_comment')
    parent = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name='parent_comment')
    reply_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="replies")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-comment_time']

