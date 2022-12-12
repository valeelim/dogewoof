from django.urls import path
from supplies.views import  show_supplies, show_json ,add_product, add

app_name = 'supplies'

urlpatterns = [
    #Leave as empty string for base url
    path('', show_supplies, name='show_supplies'),
    path('json/', show_json, name='show_json'),
    path('add/', add_product, name='add_product'),
    path('add-flutter/', add, name='add'),
    # path('ubah-status/<int:id>', ubah_status, name='ubah_status'),
    # path('hapus-task/<int:id>', hapus_task, name='hapus_task'),

]