from rest_framework import serializers
from .models import Message, MessageGroup
from datetime import datetime, timezone
from django.utils.timesince import timesince

class MessageGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageGroup
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender_nickname = serializers.CharField(source='sender.nickname', read_only=True)
    sender_role = serializers.CharField(source='sender.role.name', read_only=True)  # From Role FK
    time_ago = serializers.SerializerMethodField()  # for "2 minutes ago"

    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_nickname', 'sender_role', 'group', 'content', 'timestamp', 'time_ago']

    def get_time_ago(self, obj):
        return timesince(obj.timestamp, datetime.now(timezone.utc)) + " ago"
