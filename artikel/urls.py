from django.urls import path
from artikel.views import show_artikel, show_bulldog, show_chihuahua, show_chowchow, show_germanshepherd,show_huskey, show_pomeranians, show_poodles, show_shihtzu


app_name = 'artikel'

urlpatterns = [
    path('', show_artikel, name='show_artikel'),
    path('huskey/',show_huskey, name='show_huskey'),
    path('bulldog/',show_bulldog, name='show_bulldog'),
    path('germanshepherd/',show_germanshepherd, name='show_germanshepherd'),
    path('poodles/',show_poodles, name='show_poodles'),
    path('shihtzu/',show_shihtzu, name='show_shihtzu'),
    path('pomeranians/',show_pomeranians, name='show_pomeranians'),
    path('chihuahua/',show_chihuahua, name='show_chihuahua'),
    path('chowchow/',show_chowchow, name='show_chowchow'),
]