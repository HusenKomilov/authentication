from django.urls import path
from .views import ToConnectAPIView

urlpatterns = [path('to-connect/', ToConnectAPIView.as_view())]