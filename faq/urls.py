from django.urls import path
from faq.views import mainpage, input_question



app_name = 'faq'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('input_question/', input_question, name='input_question'),
]