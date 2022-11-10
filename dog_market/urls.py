from django.urls import path
from dog_market.views import *

app_name = 'dog_market'
urlpatterns = [
    path('', listing, name="listing"),
    path('submit_item/', submit_item, name="submit_item"),
    path('submit_item_alt/', submit_item_alt, name="submit_item_alt"),
    path('view_item/<int:itemid>/', view_item, name="view_item"),

    # path('view_item/', view_item, name="view_item"),

]