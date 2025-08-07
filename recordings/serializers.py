from rest_framework import serializers
from .models import Recording, RecordingShare
from core.models import User

class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = '__all__'

class RecordingShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordingShare
        fields = '__all__'

# --- Show nickname when listing shared users -----
class RecordingShareDetailSerializer(serializers.ModelSerializer):
    shared_with_user_nickname = serializers.CharField(source='shared_with_user.nickname', read_only=True)

    class Meta:
        model = RecordingShare
        fields = ['id', 'recording', 'shared_with_user', 'shared_with_user_nickname', 'shared_at']
