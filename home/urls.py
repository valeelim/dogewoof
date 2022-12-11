from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contactUs, name='contact_us'),
    path('make-donation/', views.makeDonation, name='make_donation'),
    path('get-donation-sum/', views.getDonation, name='get_donation_sum'),
    path('get-all-donations/', views.getAllDonations, name='get_all_donations'),
]