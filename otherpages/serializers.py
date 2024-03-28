from rest_framework import serializers
from .models import ToConnect, LiveStream


class LiveStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStream
        fields = (
            'id',
            'title',
            'twitch_stream_url',
            'created_at',
            'updated_at',
        )


class ToConnectSerializer(serializers.ModelSerializer):
    # livestream = LiveStreamSerializer()

    class Meta:
        model = ToConnect
        fields = (
            'id',
            'name',
            'phone_number',
            'complaint',
            'is_agree',
            #'livestream',
            'created_at',
            'updated_at',
        )

