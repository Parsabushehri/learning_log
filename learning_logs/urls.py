''' Define URL patterns for learning_lgos '''

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),

    #single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]