from django.urls import path
from supplies.views import add_product, show_supplies
from supplies.views import show_json 
from supplies.views import view_product 
from supplies.views import login_user


app_name = 'supplies'
urlpatterns = [
    #Leave as empty string for base url
    path('', show_supplies, name='show_supplies'),
    path('json/', show_json, name='show_json'),
    # path('cart/', cart, name='cart'),
    path('view_product/', view_product, name='view_product'),
    
    path('add-product/', add_product, name='add_product'),

    path('login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),
    
]