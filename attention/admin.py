from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Attention)
class AttentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'attention_time')
