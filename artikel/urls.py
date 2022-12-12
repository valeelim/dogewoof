from django.urls import path
from artikel.views import *



app_name = 'artikel'

urlpatterns = [
    path('model-json/',get_model_json, name='get_model_json'),
    path('', show_dog_list, name='show_artikel'),
    path('get-dog-detail/<id>/', get_dog_detail, name="get_dog_detail" ),
    path('get-dog-detail-json/<id>/', get_dog_detail_json, name="get_dog_detail_json" )

]