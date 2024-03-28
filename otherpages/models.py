from django.db import models
from utils.models import BaseModel


class ToConnect(BaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    complaint = models.TextField()

    is_agree = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LiveStream(BaseModel):
    title = models.CharField(max_length=255)

    twitch_stream_url = models.URLField()

    def __str__(self):
        return self.title
