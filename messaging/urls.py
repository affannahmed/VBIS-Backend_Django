from django.urls import path
from .views import (
    MessageListCreateAPIView,
    MessageRetrieveUpdateDestroyAPIView,
    MessageGroupListCreateAPIView,
    MessageGroupRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('message/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('message/<uuid:pk>/', MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-detail'),

    path('groups/', MessageGroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/<uuid:pk>/', MessageGroupRetrieveUpdateDestroyAPIView.as_view(), name='group-detail'),
]
