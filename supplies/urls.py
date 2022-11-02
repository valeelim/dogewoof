from django.urls import path
from supplies.views import  show_supplies, show_json ,add_product, ubah_status, hapus_task
# from supplies.views import view_product 

app_name = 'supplies'

urlpatterns = [
    #Leave as empty string for base url
    path('', show_supplies, name='show_supplies'),

    path('json/', show_json, name='show_json'),
    path('add/', add_product, name='add_product'),
    path('ubah-status/<int:id>', ubah_status, name='ubah_status'),
    path('hapus-task/<int:id>', hapus_task, name='hapus_task'),

]