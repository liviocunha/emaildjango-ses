from django.contrib import admin
from django.urls import path, include
from core import views
from django_ses.views import SESEventWebhookView

urlpatterns = [
    path('', views.index),
    path('send-email/', views.send_email, name='send-email'),
    path('reporting/', include('django_ses.urls')),
    path('event-webhook/', SESEventWebhookView.as_view(), name='event_webhook')
]
