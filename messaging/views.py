from rest_framework import generics
from .models import Message, MessageGroup
from .serializers import MessageSerializer, MessageGroupSerializer

# MESSAGES
class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

class MessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# GROUPS
class MessageGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = MessageGroup.objects.all()
    serializer_class = MessageGroupSerializer

class MessageGroupRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageGroup.objects.all()
    serializer_class = MessageGroupSerializer

from rest_framework import generics
from .models import Message, MessageGroup
from .serializers import MessageSerializer, MessageGroupSerializer

# MESSAGES
class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all().order_by('-timestamp')
        group_id = self.request.query_params.get('group')
        if group_id:
            queryset = queryset.filter(group__id=group_id)
        return queryset
