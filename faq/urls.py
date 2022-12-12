from django.urls import path
from faq.views import mainpage, input_question, json_forum



app_name = 'faq'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('input_question/', input_question, name='input_question'),
    path('json/', json_forum, name='json_forum'),
]